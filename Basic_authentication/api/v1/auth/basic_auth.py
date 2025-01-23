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
