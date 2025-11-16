#!/usr/bin/env python3
"""
AppTweak to Google Ads Keyword Exporter

This script connects to the AppTweak API, fetches casino-related keyword suggestions,
and exports them to a CSV file in Google Ads format.
"""

import os
import csv
import requests
import argparse
from typing import List, Dict, Optional
from datetime import datetime


class AppTweakKeywordExporter:
    """Main class for fetching keywords from AppTweak and exporting to Google Ads CSV."""
    
    BASE_URL = "https://api.apptweak.com"
    
    def __init__(self, api_key: str):
        """
        Initialize the exporter with AppTweak API key.
        
        Args:
            api_key: Your AppTweak API token
        """
        self.api_key = api_key
        self.headers = {
            "X-Apptweak-Key": api_key,
            "Content-Type": "application/json"
        }
    
    def fetch_keyword_suggestions(
        self,
        country: str = "us",
        language: str = "en",
        category: str = "casino",
        limit: int = 100
    ) -> List[Dict]:
        """
        Fetch keyword suggestions from AppTweak API.
        
        Args:
            country: Country code (default: "us")
            language: Language code (default: "en")
            category: App category (default: "casino")
            limit: Maximum number of keywords to fetch (default: 100)
        
        Returns:
            List of keyword dictionaries
        """
        url = f"{self.BASE_URL}/api/public/keywords/suggestions.json"
        params = {
            "country": country,
            "language": language,
            "category": category,
            "limit": limit
        }
        
        try:
            print(f"Fetching keywords from AppTweak API...")
            print(f"Parameters: country={country}, language={language}, category={category}, limit={limit}")
            
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract keywords from the response
            keywords = []
            if isinstance(data, dict):
                # Handle different possible response structures
                if "keywords" in data:
                    keywords = data["keywords"]
                elif "results" in data:
                    keywords = data["results"]
                elif "suggestions" in data:
                    keywords = data["suggestions"]
                else:
                    # If the response is a list of keywords directly
                    keywords = data if isinstance(data, list) else []
            elif isinstance(data, list):
                keywords = data
            
            print(f"Successfully fetched {len(keywords)} keywords")
            return keywords
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching keywords: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response status: {e.response.status_code}")
                print(f"Response body: {e.response.text}")
            raise
    
    def format_for_google_ads(
        self,
        keywords: List[Dict],
        campaign_name: str = "Casino Campaign",
        ad_group_name: str = "Casino Keywords",
        match_type: str = "Broad",
        max_cpc: str = "1.00",
        final_url: Optional[str] = None
    ) -> List[Dict]:
        """
        Format keywords for Google Ads CSV import.
        
        Args:
            keywords: List of keyword dictionaries from AppTweak
            campaign_name: Name of the Google Ads campaign
            ad_group_name: Name of the ad group
            match_type: Match type (Broad, Phrase, or Exact)
            max_cpc: Maximum cost per click in USD
            final_url: Optional final URL for the keywords
        
        Returns:
            List of formatted keyword dictionaries
        """
        formatted_keywords = []
        
        for keyword_data in keywords:
            # Extract keyword text from various possible structures
            keyword_text = None
            if isinstance(keyword_data, dict):
                keyword_text = (
                    keyword_data.get("keyword") or
                    keyword_data.get("term") or
                    keyword_data.get("text") or
                    keyword_data.get("name") or
                    str(keyword_data)
                )
            elif isinstance(keyword_data, str):
                keyword_text = keyword_data
            else:
                keyword_text = str(keyword_data)
            
            if not keyword_text:
                continue
            
            # Create Google Ads formatted row
            formatted_row = {
                "Campaign": campaign_name,
                "Ad Group": ad_group_name,
                "Keyword": keyword_text.strip(),
                "Match Type": match_type,
                "Max CPC": max_cpc,
                "Final URL": final_url or "",
                "Status": "Active"
            }
            
            formatted_keywords.append(formatted_row)
        
        return formatted_keywords
    
    def export_to_csv(
        self,
        formatted_keywords: List[Dict],
        output_file: str = "google_ads_keywords.csv"
    ) -> str:
        """
        Export formatted keywords to CSV file in Google Ads format.
        
        Args:
            formatted_keywords: List of formatted keyword dictionaries
            output_file: Output CSV file path
        
        Returns:
            Path to the created CSV file
        """
        if not formatted_keywords:
            raise ValueError("No keywords to export")
        
        # Google Ads CSV headers
        fieldnames = [
            "Campaign",
            "Ad Group",
            "Keyword",
            "Match Type",
            "Max CPC",
            "Final URL",
            "Status"
        ]
        
        # Write to CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(formatted_keywords)
        
        print(f"Exported {len(formatted_keywords)} keywords to {output_file}")
        return output_file


def main():
    """Main function to run the keyword exporter."""
    parser = argparse.ArgumentParser(
        description="Export casino-related keywords from AppTweak to Google Ads CSV format"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help="AppTweak API key (or set APPTWEAK_API_KEY environment variable)",
        default=os.getenv("APPTWEAK_API_KEY")
    )
    parser.add_argument(
        "--country",
        type=str,
        default="us",
        help="Country code (default: us)"
    )
    parser.add_argument(
        "--language",
        type=str,
        default="en",
        help="Language code (default: en)"
    )
    parser.add_argument(
        "--category",
        type=str,
        default="casino",
        help="App category (default: casino)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Maximum number of keywords to fetch (default: 100)"
    )
    parser.add_argument(
        "--campaign",
        type=str,
        default="Casino Campaign",
        help="Google Ads campaign name (default: Casino Campaign)"
    )
    parser.add_argument(
        "--ad-group",
        type=str,
        default="Casino Keywords",
        help="Google Ads ad group name (default: Casino Keywords)"
    )
    parser.add_argument(
        "--match-type",
        type=str,
        choices=["Broad", "Phrase", "Exact"],
        default="Broad",
        help="Keyword match type (default: Broad)"
    )
    parser.add_argument(
        "--max-cpc",
        type=str,
        default="1.00",
        help="Maximum cost per click in USD (default: 1.00)"
    )
    parser.add_argument(
        "--final-url",
        type=str,
        default=None,
        help="Final URL for keywords (optional)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output CSV file path (default: google_ads_keywords_TIMESTAMP.csv)"
    )
    
    args = parser.parse_args()
    
    # Validate API key
    if not args.api_key:
        print("Error: AppTweak API key is required.")
        print("Set it via --api-key argument or APPTWEAK_API_KEY environment variable")
        return 1
    
    # Generate output filename if not provided
    if not args.output:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.output = f"google_ads_keywords_{timestamp}.csv"
    
    try:
        # Initialize exporter
        exporter = AppTweakKeywordExporter(args.api_key)
        
        # Fetch keywords
        keywords = exporter.fetch_keyword_suggestions(
            country=args.country,
            language=args.language,
            category=args.category,
            limit=args.limit
        )
        
        if not keywords:
            print("Warning: No keywords were fetched from the API")
            return 1
        
        # Format for Google Ads
        formatted_keywords = exporter.format_for_google_ads(
            keywords=keywords,
            campaign_name=args.campaign,
            ad_group_name=args.ad_group,
            match_type=args.match_type,
            max_cpc=args.max_cpc,
            final_url=args.final_url
        )
        
        # Export to CSV
        output_path = exporter.export_to_csv(formatted_keywords, args.output)
        
        print(f"\n✓ Success! Keywords exported to: {output_path}")
        print(f"  Total keywords: {len(formatted_keywords)}")
        print(f"  Campaign: {args.campaign}")
        print(f"  Ad Group: {args.ad_group}")
        print(f"  Match Type: {args.match_type}")
        print(f"\nYou can now import this CSV file into Google Ads Editor.")
        
        return 0
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())

