#!/usr/bin/env python3
"""GitHub Gists API Server - Simple Flask web server for GitHub Gists"""

import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/<username>')
def get_gists(username):
    try:
        github_api_url = f'https://api.github.com/users/{username}/gists'
        response = requests.get(github_api_url)
        
        if response.status_code == 200:
            gists = response.json()
            result = []
            for gist in gists:
                result.append({
                    'id': gist.get('id'),
                    'description': gist.get('description') or 'No description',
                    'url': gist.get('html_url')
                })
            return jsonify(result)
        elif response.status_code == 404:
            return jsonify({'error': 'User not found'}), 404
        else:
            return jsonify({'error': 'API error'}), 500
            
    except Exception:
        return jsonify({'error': 'Service unavailable'}), 503



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))