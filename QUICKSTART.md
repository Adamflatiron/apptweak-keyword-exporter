# Quick Start Guide

Get up and running in 3 steps!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Set Your API Key

**Option A: Environment Variable (Recommended)**
```bash
export APPTWEAK_API_KEY="your_api_key_here"
```

**Option B: Command Line**
Just pass `--api-key YOUR_KEY` when running the script.

## Step 3: Run the Script

```bash
python keyword_exporter.py
```

That's it! The script will:
1. Fetch casino-related keywords from AppTweak
2. Format them for Google Ads
3. Export to a CSV file (e.g., `google_ads_keywords_20240101_120000.csv`)

## Next Steps

1. **Import to Google Ads Editor**: Open the CSV file in Google Ads Editor
2. **Review Keywords**: Check the keywords and adjust as needed
3. **Upload**: Upload the changes to your Google Ads account

## Customization

Want to customize? Here are some common options:

```bash
# More keywords
python keyword_exporter.py --limit 500

# Different match type
python keyword_exporter.py --match-type Exact

# Custom campaign name
python keyword_exporter.py --campaign "My Casino Campaign"

# Higher CPC
python keyword_exporter.py --max-cpc 5.00
```

See `README.md` for all available options!

