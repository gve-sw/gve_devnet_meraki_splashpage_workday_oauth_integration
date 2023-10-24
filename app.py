""" Copyright (c) 2023 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied."""

# Import necessary libraries and modules
from flask import Flask, redirect, request, render_template_string, session, url_for
from flask_oauthlib.client import OAuth
import requests

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for Flask sessions. Change this to a secure random value.

# Initialize OAuth for Flask
oauth = OAuth(app)

# Define Workday OAuth configuration
workday = oauth.remote_app(
    'workday',
    consumer_key='YOUR_WORKDAY_CLIENT_ID',  # Workday OAuth client ID
    consumer_secret='YOUR_WORKDAY_CLIENT_SECRET',  # Workday OAuth client secret
    request_token_params={'scope': 'openid profile'},  # OAuth scopes
    base_url='https://your-workday-domain.com/',  # Base URL for Workday
    request_token_url=None,  # No request token URL for OAuth 2.0
    access_token_method='POST',  # HTTP method for obtaining access token
    access_token_url='https://your-workday-domain.com/oauth2/token',  # URL to obtain access token
    authorize_url='https://your-workday-domain.com/oauth2/authorize'  # URL for authorization
)

# Define Meraki API key and network ID
MERAKI_API_KEY = 'YOUR_MERAKI_API_KEY'
NETWORK_ID = 'YOUR_MERAKI_NETWORK_ID'

# Function to grant access to a specific client device in Meraki
def grant_access_in_meraki(client_mac_address):
    # Construct URL for Meraki API endpoint
    url = f"https://api.meraki.com/api/v1/networks/{NETWORK_ID}/clients/{client_mac_address}/policy"
    # Define policy details (modify as needed)
    policy = {
        "devicePolicy": "Group policy or SSID policy ID",
        "devicePolicyType": "Group policy or SSID policy type"
    }
    # Define headers for the API request
    headers = {
        'X-Cisco-Meraki-API-Key': MERAKI_API_KEY,
        'Content-Type': 'application/json'
    }
    # Send PUT request to Meraki API to update client policy
    response = requests.put(url, json=policy, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        return True
    else:
        return False

@app.route('/')
def index():
    # Render the captive portal page
    return render_template_string(open("captive_portal.html").read())

@app.route('/login')
def login():
    # Redirect user to Workday for OAuth authentication
    return workday.authorize(callback=url_for('authorized', _external=True))

@app.route('/login/authorized')
def authorized():
    # Handle the callback after Workday OAuth authentication
    response = workday.authorized_response()
    # Check if the authentication was successful
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )

    # Store the access token in the session
    session['workday_token'] = (response['access_token'], '')

    # Extract the client's MAC address from the Workday response (modify as per your Workday integration)
    client_mac_address = 'CLIENT_MAC_ADDRESS_FROM_WORKDAY'

    # Grant access in Meraki using the extracted MAC address
    if grant_access_in_meraki(client_mac_address):
        return 'Logged in successfully! Access granted in Meraki.'
    else:
        return 'Logged in successfully, but access was not granted in Meraki.'

@workday.tokengetter
def get_workday_oauth_token():
    # Retrieve the stored Workday OAuth token from the session
    return session.get('workday_token')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)