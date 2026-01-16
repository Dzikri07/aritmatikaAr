#!/usr/bin/env python3
"""
Simple HTTP Server for Barisan Aritmatika AR App
Run: python3 server.py
Then open: http://localhost:8000
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler

# Change to script directory
os.chdir(Path(__file__).parent.absolute())

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers untuk avoid CORS issues
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

def run_server():
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"🚀 Server running at {url}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"✅ Open browser: {url}/index.html")
        print(f"⏹️  Press Ctrl+C to stop")
        
        try:
            # Automatically open browser
            webbrowser.open(f"{url}/index.html")
        except:
            pass
        
        httpd.serve_forever()

if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
