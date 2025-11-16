# Deployment Guide

This web application can be deployed to various platforms. Here are the easiest options:

## Option 1: Render (Recommended - Free & Easy)

1. **Sign up** at [render.com](https://render.com) (free account)

2. **Create a New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository (or push this code to GitHub first)
   - Or use "Public Git repository" and paste your repo URL

3. **Configure**:
   - **Name**: `apptweak-keyword-exporter` (or any name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (or paid if you need more resources)

4. **Add Environment Variables** (if needed):
   - Go to "Environment" tab
   - Add any required variables

5. **Deploy**: Click "Create Web Service"
   - Render will automatically deploy your app
   - You'll get a URL like: `https://apptweak-keyword-exporter.onrender.com`

6. **Share the Link**: Send the URL to your boss! 🎉

## Option 2: Heroku

1. **Install Heroku CLI**: [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

2. **Login**:
   ```bash
   heroku login
   ```

3. **Create App**:
   ```bash
   heroku create apptweak-keyword-exporter
   ```

4. **Deploy**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

5. **Open**:
   ```bash
   heroku open
   ```

## Option 3: Railway

1. **Sign up** at [railway.app](https://railway.app)

2. **New Project** → "Deploy from GitHub repo"

3. **Configure**:
   - Select your repository
   - Railway auto-detects Python
   - Add start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

4. **Deploy**: Railway automatically deploys

## Option 4: PythonAnywhere

1. **Sign up** at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload files** via Files tab

3. **Create Web App**:
   - Go to Web tab
   - Click "Add a new web app"
   - Choose Flask
   - Point to your `app.py`

4. **Reload** the web app

## Option 5: Local Development (For Testing)

Run locally to test before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then visit: `http://localhost:5000`

## Quick Deploy Checklist

- [ ] Code is in a Git repository (GitHub recommended)
- [ ] `requirements.txt` includes all dependencies
- [ ] `Procfile` is present (for Heroku/Render)
- [ ] Tested locally first
- [ ] Environment variables configured (if needed)
- [ ] Deployed and tested the live URL

## Notes

- **Free tiers** usually have limitations (sleep after inactivity, slower cold starts)
- **Render** and **Railway** are great free options with good performance
- The app doesn't store any data, so no database setup needed
- API keys are entered by users in the form (not stored server-side)

## Security Note

For production, change the `app.secret_key` in `app.py` to a secure random string!

