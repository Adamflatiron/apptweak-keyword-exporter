# 🚀 Quick Deploy Guide - Share with Your Boss!

## Fastest Way: Render (5 minutes)

1. **Push to GitHub** (if not already):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Go to Render**: https://render.com
   - Sign up (free) or log in
   - Click "New +" → "Web Service"
   - Connect your GitHub repo

3. **Configure**:
   - **Name**: `apptweak-keyword-exporter` (or any name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

4. **Deploy**: Click "Create Web Service"
   - Wait 2-3 minutes for deployment
   - You'll get a URL like: `https://apptweak-keyword-exporter.onrender.com`

5. **Share the Link**: Send the URL to your boss! 🎉

## Test Locally First (Optional)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Open browser to: http://localhost:5000
```

## What Your Boss Will See

A beautiful web interface where they can:
- Enter their AppTweak API key
- Configure keyword settings (country, language, match type, etc.)
- Click "Export Keywords to CSV"
- Download a Google Ads-ready CSV file

No installation needed - just a web browser!

## Alternative: Railway (Also Free)

1. Go to https://railway.app
2. Sign up with GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Select your repo
5. Add start command: `gunicorn app:app --bind 0.0.0.0:$PORT`
6. Deploy!

## Notes

- **Free tiers** may have cold starts (first load takes a few seconds)
- **No database needed** - everything runs in memory
- **API keys** are entered by users (not stored)
- **Secure** - each user enters their own API key

## Troubleshooting

**Deployment fails?**
- Check that `requirements.txt` includes all dependencies
- Verify `Procfile` exists with: `web: gunicorn app:app`
- Check Render/Railway logs for errors

**App doesn't work?**
- Make sure `gunicorn` is in `requirements.txt`
- Verify the start command is correct
- Check the logs in your hosting platform

