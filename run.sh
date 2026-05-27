#!/bin/bash
# Start the 3D Portfolio Website

echo "🚀 Starting 3D Portfolio Website..."
echo ""
echo "Make sure you've customized app.py with your information!"
echo ""
echo "Opening http://localhost:5000 in your browser..."
echo ""
echo "To stop the server, press CTRL+C"
echo ""

cd "$(dirname "$0")"
python3 app.py
