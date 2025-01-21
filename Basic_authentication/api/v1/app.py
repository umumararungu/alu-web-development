#!/usr/bin/env python3
"""
Route module for the API
"""
from api.v1.auth.auth import Auth # type: ignore
from api.v1.auth.basic_auth import BasicAuth # type: ignore
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
if os.getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()
elif os.getlogin("AUTH_TYPE") == "auth":
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.before_request
def before():
    "before request"
    if auth:
        paths = ['/api/vi/status',
                 '/api/v1/unauthorized/']
        if not auth.require_auth(request.path, paths):
            return
        if not auth.authorization_header(request):
            abort(401)

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
