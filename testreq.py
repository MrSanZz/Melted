import os
import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, Response, request

app = Flask(__name__)
@app.route('/')
def serve_cloned_website():
    # Get the new domain from the query parameters
    new_domain = request.args.get('new_domain', '')
    
    # Serve the index.html file
    file_path = os.path.join(new_domain, 'index.html')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return Response(f.read(), mimetype='text/html')
    else:
        with open('index.html','a') as file:
            f = file.readline()
        html=f.rstrip()
        return f'{html}', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)