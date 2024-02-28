#!/usr/bin/python3
"""module contains views(route) status"""
from api.v1.views import app_views
from flask import Flask, jsonify

@app_views.route('/status', strict_slashes=False)
def status():
    """Endpoint to check the status of the API"""
    return jsonify ({"status": "OK"})
