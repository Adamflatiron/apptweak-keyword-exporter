#!/bin/bash
# Quick start script for local development

echo "🚀 Starting AppTweak Keyword Exporter..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the app
echo ""
echo "✅ Starting web server..."
echo "🌐 Open your browser to: http://localhost:5000"
echo ""
python app.py

