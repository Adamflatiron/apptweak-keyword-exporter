# How to Set Your API Key (So You Don't Have to Enter It Every Time)

## For Render Deployment

1. **Go to your Render dashboard**: https://dashboard.render.com
2. **Select your web service** (`apptweak-keyword-exporter`)
3. **Go to "Environment" tab**
4. **Add Environment Variable**:
   - **Key**: `APPTWEAK_API_KEY`
   - **Value**: Your AppTweak API key
5. **Click "Save Changes"**
6. **Redeploy** (Render will automatically redeploy when you save)

That's it! Now the API key field will be pre-filled, and you won't need to enter it every time.

## For Railway Deployment

1. **Go to your Railway project**
2. **Click on your service**
3. **Go to "Variables" tab**
4. **Add Variable**:
   - **Key**: `APPTWEAK_API_KEY`
   - **Value**: Your AppTweak API key
5. **Save** (Railway auto-redeploys)

## For Local Development

Create a `.env` file in the project folder:

```bash
APPTWEAK_API_KEY=your_api_key_here
```

Or set it in your terminal:

```bash
export APPTWEAK_API_KEY="your_api_key_here"
```

## How It Works

- If `APPTWEAK_API_KEY` is set, the form field will be **pre-filled**
- You can still **override** it by typing a different key in the form
- If the form field is empty, it will use the environment variable automatically
- If neither is set, you'll get an error asking for the API key

## Security Note

- Environment variables are **secure** - they're not visible in the code
- Only you (and people with access to your deployment dashboard) can see them
- The API key is never exposed in the frontend code

