#!/usr/bin/env python3
"""
Flask Web Application for AppTweak to Google Ads Keyword Exporter
"""

from flask import Flask, render_template, request, send_file, jsonify, session
import csv
import io
import requests
from datetime import datetime
from keyword_exporter import AppTweakKeywordExporter

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'  # Change this in production!


@app.route('/')
def index():
    """Render the main form page."""
    return render_template('index.html')


@app.route('/api/export', methods=['POST'])
def export_keywords():
    """API endpoint to fetch keywords and return CSV."""
    try:
        data = request.json
        
        # Validate required fields
        api_key = data.get('api_key')
        if not api_key:
            return jsonify({'error': 'API key is required'}), 400
        
        # Get parameters with defaults
        country = data.get('country', 'us')
        language = data.get('language', 'en')
        category = data.get('category', 'casino')
        limit = int(data.get('limit', 100))
        campaign_name = data.get('campaign', 'Casino Campaign')
        ad_group_name = data.get('ad_group', 'Casino Keywords')
        match_type = data.get('match_type', 'Broad')
        max_cpc = data.get('max_cpc', '1.00')
        final_url = data.get('final_url', '')
        
        # Initialize exporter
        exporter = AppTweakKeywordExporter(api_key)
        
        # Fetch keywords
        keywords = exporter.fetch_keyword_suggestions(
            country=country,
            language=language,
            category=category,
            limit=limit
        )
        
        if not keywords:
            return jsonify({'error': 'No keywords were fetched from the API'}), 400
        
        # Format for Google Ads
        formatted_keywords = exporter.format_for_google_ads(
            keywords=keywords,
            campaign_name=campaign_name,
            ad_group_name=ad_group_name,
            match_type=match_type,
            max_cpc=max_cpc,
            final_url=final_url if final_url else None
        )
        
        # Create CSV in memory
        output = io.StringIO()
        fieldnames = ['Campaign', 'Ad Group', 'Keyword', 'Match Type', 'Max CPC', 'Final URL', 'Status']
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(formatted_keywords)
        
        # Create file-like object for download
        mem = io.BytesIO()
        mem.write(output.getvalue().encode('utf-8'))
        mem.seek(0)
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"google_ads_keywords_{timestamp}.csv"
        
        return send_file(
            mem,
            mimetype='text/csv',
            as_attachment=True,
            download_name=filename
        )
        
    except requests.exceptions.RequestException as e:
        error_msg = str(e)
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_data = e.response.json()
                error_msg = error_data.get('message', error_msg)
            except:
                error_msg = e.response.text or error_msg
        return jsonify({'error': f'API Error: {error_msg}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

