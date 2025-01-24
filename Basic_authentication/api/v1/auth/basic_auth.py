#!/usr/bin/env python3
'''çomment'''


from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''extact base function'''
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        '''other function'''
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        base64_encoded = base64_authorization_header

        try:
            decoded_value = base64.b64decode(base64_encoded).decode('utf-8')
            return decoded_value
        except (ValueError, UnicodeDecodeError):
            return None

        return decoded_value

    def extract_user_credentials(self,
        decoded_base64_authorization_header: str) -> (str, str):
        """extract function
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        base64_decoded = decoded_base64_authorization_header

        if ":" not in base64_decoded:
            return None, None

        usr_email, usr_password = base64_decoded.split(':', 1)
        return usr_email, usr_password
