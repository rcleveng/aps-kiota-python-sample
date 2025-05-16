import os
from kiota_abstractions.authentication.anonymous_authentication_provider import AuthenticationProvider, RequestInformation

class BearerTokenAuthenticationProvider(AuthenticationProvider):
    def __init__(self, access_token: str = None) -> None:
        self.access_token = access_token or os.environ.get("APS_ACCESS_TOKEN")
        if not self.access_token:
            raise ValueError("Please provide a valid access token")

    async def authenticate_request(self, request: RequestInformation, additional_authentication_context: dict[str, any] = {}) -> None:
        # TODO: check whether the token is valid for the request
        request.headers.add("Authorization", f"Bearer {self.access_token}")