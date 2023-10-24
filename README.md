# gve_devnet_meraki_splashpage_workday_oauth_integration

This project offers a Flask-based application that integrates a Meraki wireless network with Workday OAuth authentication. Users can seamlessly access the network without manual intervention after verifying their identity with Workday.

## Contacts
- Rey Diaz

## Solution Components
- Meraki
- Workday OAuth
- Flask


> **Note:** The current implementation focuses on the Meraki integration and is missing the specific details and logic related to the Workday portion. The Workday integration will need to be completed for full functionality.


## Prerequisites
### Meraki API Keys
To utilize the Meraki API, enable the API for your organization and generate an API key. Follow these steps:
1. Login to the Meraki dashboard.
2. Navigate to `Organization > Settings > Dashboard API access`.
3. Enable the Cisco Meraki Dashboard API.
4. Go to `My Profile > API access` and generate the API key.
6. Store the API key securely.

### Workday OAuth Configuration
Ensure you have the necessary OAuth credentials from Workday, including the Client ID, Client Secret, and appropriate Workday domain.

## Installation/Configuration
1. Clone this repository.
2. Add Meraki API key to environment variables.
3. Set up a Python virtual environment and ensure Python 3 is installed.
4. Install the required packages.

## Usage
Run the application with the command: `$ python3 app.py`

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:

Please note: This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
