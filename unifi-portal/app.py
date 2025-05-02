# app.py for UniFi Captive Portal Add-on

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the UniFi Captive Portal!"

@app.route('/connect', methods=['POST'])
def connect():
    data = request.json
    unifi_url = data.get('unifi_controller_url')
    username = data.get('unifi_username')
    password = data.get('unifi_password')

    # Example: Authenticate with UniFi Controller (pseudo-code)
    response = requests.post(f"{unifi_url}/api/login", json={"username": username, "password": password})
    if response.status_code == 200:
        return jsonify({"message": "Connected to UniFi WiFi!"})
    else:
        return jsonify({"error": "Failed to connect."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)