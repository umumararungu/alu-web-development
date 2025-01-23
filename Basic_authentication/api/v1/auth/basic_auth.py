#!/usr/bin/env python3
'''çomment'''


from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class.
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''extact base function'''
        if authorization_header is None:
            return None

        elif authorization_header is not str:
            return None

        elif authorization_header.DoesNotStartWith('Basic') and authorization_header.Endswith(" "):
            return None

        else:
            return authorization_header
