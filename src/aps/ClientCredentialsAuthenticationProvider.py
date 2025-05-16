import os
import requests
from kiota_abstractions.authentication.anonymous_authentication_provider import AuthenticationProvider, RequestInformation

class ClientCredentialsAuthenticationProvider(AuthenticationProvider):
    def __init__(self, client_id: str = None, client_secret: str = None) -> None:
        self.client_id = client_id or os.environ.get("APS_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("APS_CLIENT_SECRET")
        if not self.client_id or not self.client_secret:
            raise ValueError("Please provide a valid client ID and client secret")

    async def authenticate_request(self, request: RequestInformation, additional_authentication_context: dict[str, any] = {}) -> None:
        access_token = self.generate_access_token(self.client_id, self.client_secret, "bucket:read data:read")
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