#!/usr/bin/python3
from flask import jsonify
from api.v1.app import app_views

@app_views.route("/status", methods=["GET"])
def status():
    """reports the status of ..."""
    return jsonify({"status": "OK"})
