import base64

from fastapi import HTTPException
import requests

from app.config import CISCO_IDP_TOKEN_URL, CLIENT_ID, CLIENT_SECRET


class CiscoIDPService:
    @staticmethod
    def _get_encoded_credentials() -> str:
        return base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode("utf-8")).decode(
            "utf-8"
        )

    @staticmethod
    def _get_token_response() -> str:
        encoded_credentials = CiscoIDPService._get_encoded_credentials()
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded_credentials}",
        }
        token_response = requests.post(
            CISCO_IDP_TOKEN_URL, headers=headers, data="grant_type=client_credentials"
        )
        return token_response.json()

    @staticmethod
    def get_access_token() -> str:
        token_response = CiscoIDPService._get_token_response()
        if token_response.get("access_token") is None:
            raise HTTPException(
                status_code=401,
                detail="Failed to obtain access token from Cisco IDP Service.",
            )
        return token_response.get("access_token")
