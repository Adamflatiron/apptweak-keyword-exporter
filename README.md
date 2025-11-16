# AppTweak to Google Ads Keyword Exporter

A web application and Python tool that connects to the AppTweak API, fetches casino-related keyword suggestions, and exports them to a CSV file in Google Ads format.

## 🌐 Web Application (Recommended)

**Share a link with your team!** This tool includes a beautiful web interface that you can deploy and share via URL.

### Quick Deploy Options:

1. **Render** (Free & Easy) - See [DEPLOY.md](DEPLOY.md) for instructions
2. **Heroku** - See [DEPLOY.md](DEPLOY.md) for instructions  
3. **Railway** - See [DEPLOY.md](DEPLOY.md) for instructions

Once deployed, you'll get a shareable URL like: `https://your-app.onrender.com`

### Local Web Server:

Run the web app locally:
```bash
pip install -r requirements.txt
python app.py
```

Then visit: `http://localhost:5000`

---

## 💻 Command Line Tool

For developers who prefer command-line usage:

## Features

- 🔌 Connects to AppTweak API to fetch keyword suggestions
- 🎰 Focuses on casino-related keywords (configurable)
- 📊 Exports to Google Ads CSV format for easy import
- ⚙️ Highly configurable (campaign, ad group, match type, CPC, etc.)
- 📝 Command-line interface for easy automation
- 🔒 Secure API key management via environment variables

## Prerequisites

1. **AppTweak API Access**: You need an AppTweak account with API access. Sign up at [AppTweak](https://www.apptweak.com/) and get your API key from the dashboard.

2. **Python 3.7+**: Make sure you have Python 3.7 or higher installed.

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Option 1: Environment Variable (Recommended)

Set your AppTweak API key as an environment variable:

```bash
# On macOS/Linux
export APPTWEAK_API_KEY="your_api_key_here"

# On Windows (PowerShell)
$env:APPTWEAK_API_KEY="your_api_key_here"
```

### Option 2: Command Line Argument

Pass the API key directly via the `--api-key` argument (see Usage below).

## Usage

### Basic Usage

```bash
python keyword_exporter.py --api-key YOUR_API_KEY
```

This will:
- Fetch casino-related keywords from AppTweak (US, English)
- Export them to a CSV file named `google_ads_keywords_TIMESTAMP.csv`
- Use default settings (Broad match type, $1.00 max CPC)

### Advanced Usage

```bash
python keyword_exporter.py \
  --api-key YOUR_API_KEY \
  --country us \
  --language en \
  --category casino \
  --limit 200 \
  --campaign "My Casino Campaign" \
  --ad-group "Casino Keywords" \
  --match-type Phrase \
  --max-cpc 2.50 \
  --final-url "https://example.com" \
  --output my_keywords.csv
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--api-key` | AppTweak API key (or use `APPTWEAK_API_KEY` env var) | Required |
| `--country` | Country code (e.g., us, gb, ca) | `us` |
| `--language` | Language code (e.g., en, es, fr) | `en` |
| `--category` | App category | `casino` |
| `--limit` | Maximum number of keywords to fetch | `100` |
| `--campaign` | Google Ads campaign name | `Casino Campaign` |
| `--ad-group` | Google Ads ad group name | `Casino Keywords` |
| `--match-type` | Match type: Broad, Phrase, or Exact | `Broad` |
| `--max-cpc` | Maximum cost per click in USD | `1.00` |
| `--final-url` | Final URL for keywords (optional) | None |
| `--output` | Output CSV file path | Auto-generated with timestamp |

## Output Format

The script generates a CSV file with the following columns:

- **Campaign**: Your Google Ads campaign name
- **Ad Group**: Your ad group name
- **Keyword**: The keyword text
- **Match Type**: Broad, Phrase, or Exact
- **Max CPC**: Maximum cost per click
- **Final URL**: Landing page URL (if provided)
- **Status**: Active

## Importing to Google Ads

1. **Open Google Ads Editor** (download from [Google Ads Editor](https://ads.google.com/home/tools/ads-editor/))

2. **Import the CSV**:
   - Open your Google Ads account in the Editor
   - Go to `Account` > `Import` > `From file...`
   - Select your generated CSV file
   - Review the import summary
   - Click `Apply` to import the keywords

3. **Review and Adjust**:
   - Review the imported keywords
   - Adjust bids, match types, or other settings as needed
   - Upload changes to your Google Ads account

## Examples

### Example 1: Basic Export
```bash
export APPTWEAK_API_KEY="your_key_here"
python keyword_exporter.py
```

### Example 2: Export with Custom Settings
```bash
python keyword_exporter.py \
  --api-key YOUR_KEY \
  --limit 500 \
  --match-type Exact \
  --max-cpc 3.00 \
  --campaign "Premium Casino Campaign"
```

### Example 3: Different Country/Language
```bash
python keyword_exporter.py \
  --api-key YOUR_KEY \
  --country gb \
  --language en \
  --category casino
```

## Troubleshooting

### Error: "AppTweak API key is required"
- Make sure you've set the `APPTWEAK_API_KEY` environment variable, or
- Pass the API key via `--api-key` argument

### Error: "Error fetching keywords"
- Verify your API key is correct
- Check your internet connection
- Ensure you have API access in your AppTweak subscription
- Check AppTweak API status and rate limits

### No keywords returned
- Verify the category name is correct
- Try different country/language combinations
- Check if there are keywords available for your selected parameters

### CSV import fails in Google Ads
- Ensure the CSV file is properly formatted (UTF-8 encoding)
- Verify all required columns are present
- Check that match types are valid (Broad, Phrase, Exact)
- Ensure CPC values are in correct format (e.g., "1.00" not "1")

## API Rate Limits

Be aware of AppTweak's API rate limits. If you exceed the limit, you may need to:
- Wait before making another request
- Upgrade your AppTweak subscription
- Reduce the `--limit` parameter

## Security Notes

- **Never commit your API key** to version control
- Use environment variables for API keys in production
- Keep your `.env` file in `.gitignore` if using one

## License

This tool is provided as-is for your use. Make sure to comply with:
- AppTweak API Terms of Service
- Google Ads Terms of Service
- Applicable regional regulations for casino advertising

## Support

For issues related to:
- **AppTweak API**: Contact [AppTweak Support](https://www.apptweak.com/support)
- **Google Ads**: Check [Google Ads Help Center](https://support.google.com/google-ads)
- **This Tool**: Open an issue in the repository

## Contributing

Feel free to fork this repository and submit pull requests for improvements!

