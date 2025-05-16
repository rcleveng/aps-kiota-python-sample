import os
import requests
from kiota_abstractions.authentication.anonymous_authentication_provider import AuthenticationProvider, RequestInformation

class ClientCredentialsAuthenticationProvider(AuthenticationProvider):
    """
    Kiota authentication provider used to authenticate requests to APS using the "client credentials" OAuth flow.
    It requires a client ID and client secret, which can be provided directly or through environment variables.
    """
    def __init__(self, client_id: str | None = None, client_secret: str | None = None, scopes: str = "data:read") -> None:
        self.client_id = client_id or os.environ.get("APS_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("APS_CLIENT_SECRET")
        self.scopes = scopes
        if not self.client_id or not self.client_secret:
            raise ValueError("Please provide a valid client ID and client secret")

    async def authenticate_request(self, request: RequestInformation, additional_authentication_context = {}) -> None:
        access_token = self.generate_access_token(self.client_id, self.client_secret, self.scopes)
        request.headers.add("Authorization", f"Bearer {access_token}")

    def generate_access_token(self, client_id, client_secret, scopes) -> str:
        url = "https://developer.api.autodesk.com/authentication/v2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
            "scope": scopes
        }
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        access_token = response.json().get("access_token")
        if not access_token:
            raise ValueError("Failed to generate access token")
        return access_token