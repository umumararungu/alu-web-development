#!/usr/bin/env python3
'''auth class'''


from flask import request
from typing import List, TypeVar


class Auth:
    '''first auth class'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''require auth function'''
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            normal_path = path + '/'
        else:
            normal_path = path

        for excluded in excluded_paths:
            if normal_path.startswith(excluded):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        '''authorization header function'''
        if request is None:
            return None
        elif not request.headers.get("Authorization"):
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        '''current user fucntion'''
        return None
