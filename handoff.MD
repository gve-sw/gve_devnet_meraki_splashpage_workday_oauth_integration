# Detailed Handoff: Workday OAuth Integration with Meraki Captive Portal

## Introduction:
This prototype is a Flask-based application designed to authenticate users on a Meraki wireless network using Workday OAuth credentials. The goal is to provide seamless access to the network without manual intervention once users authenticate with their Workday credentials.

## Key Components:

### 1. Flask Application (`app.py`):
- Serves as the core of the integration, handling web requests and orchestrating the authentication flow.
- Uses the Flask-OAuthlib library to simplify OAuth integration.

### 2. Meraki Splash Page (`captive_portal.html`):
- The initial interface users encounter when attempting to connect to the Meraki network.
- Contains a link that initiates the Workday OAuth process.

## Workday Integration Points:

### 1. OAuth Configuration:
- The application is pre-configured to integrate with Workday OAuth. However, specific details need to be filled in:
  - `YOUR_WORKDAY_CLIENT_ID`: Replace with the Client ID provided by Workday during the OAuth application setup.
  - `YOUR_WORKDAY_CLIENT_SECRET`: Substitute with the Client Secret, also provided by Workday.
  - `https://your-workday-domain.com/`: Update with the correct domain for your Workday instance.

### 2. User Authentication Flow:
- Users click on the "Login with Workday" link on the splash page, which directs them to the `/login` route.
- This route redirects users to Workday's OAuth authorization page.
- After users authenticate and grant permission, Workday redirects them back to the `/login/authorized` route, carrying an access token.

### 3. User Identification:
- Post-authentication, the application needs to identify the user or device to grant network access. 
- The placeholder `CLIENT_MAC_ADDRESS_FROM_WORKDAY` in the `/login/authorized` route is where the logic to extract the user's unique identifier (e.g., MAC address) from the Workday response should be implemented.

## Tasks for Workday Integration:

### 1. OAuth Application Setup:
- If not already done, set up an OAuth application within Workday.
- Ensure the application's redirect URI matches the `/login/authorized` route of the Flask app.

### 2. Populate OAuth Configuration:
- Update the placeholders in `app.py` with the appropriate values from the Workday OAuth application setup.

### 3. User Data Extraction:
- Modify the logic in the `/login/authorized` route to extract necessary user data from the Workday OAuth response. This could include the user's name, email, role, and any other relevant attributes.

### 4. Testing:
- Thoroughly test the authentication flow to ensure users are correctly redirected to Workday, can authenticate, and are then granted access to the Meraki network.

## Additional Considerations:

### 1. Security:
- Ensure the Flask secret key is securely generated and stored.
- Consider implementing token refresh logic to handle Workday OAuth token expiration.
- Ensure all communication is over HTTPS, especially in a production environment.

### 2. Error Handling:
- Enhance error handling for scenarios like failed authentication, token expiration, or API errors.

### 3. Documentation:
- Document any changes or additions made during the Workday integration for future reference.