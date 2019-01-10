"""
This file contains all the methods for this KBase SDK module.
"""
import requests


def echo(params):
    """Echo back the given message."""
    resp = requests.get("http://10.58.1.211:8529")
    return resp.text
