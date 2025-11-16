# Simple Steps to Deploy

## Step 1: Push to GitHub (2 minutes)

**If Source Control doesn't work, use the Terminal method:**

1. **Create repo on GitHub**: https://github.com/new
   - Name: `apptweak-keyword-exporter`
   - Don't check "Initialize with README"
   - Click "Create repository"

2. **In Cursor's Terminal** (View → Terminal, or `` Ctrl+` ``):
   ```bash
   cd /Users/adam/apptweak-keyword-exporter
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR-USERNAME/apptweak-keyword-exporter.git
   git branch -M main
   git push -u origin main
   ```
   (Replace `YOUR-USERNAME` with your GitHub username)

✅ Done! Your code is on GitHub.

**See ALTERNATIVE_WAYS.md for more options!**

---

## Step 2: Deploy to Render (3 minutes)

1. Go to **https://render.com** and sign up (free)
2. Click **"New +"** → **"Web Service"**
3. Connect your **GitHub** account
4. Select your **`apptweak-keyword-exporter`** repository
5. Click **"Create Web Service"**
6. Wait 2 minutes
7. **Copy your URL** (like: `https://apptweak-keyword-exporter.onrender.com`)

✅ Done! Share that URL with your boss.

---

## That's it!

Your boss can now:
- Open the URL in any browser
- Enter their AppTweak API key
- Download Google Ads CSV files

No installation needed!

