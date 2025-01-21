#!usr/bin/env pytho3
'''auth class'''


from flask import request
from typing import List,TypeVar


class auth():
    '''first auth class'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        