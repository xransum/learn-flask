"""Flask Unique URLs and Redirects.

This module demonstrates how to create unique URLs
and redirects in Flask.

The two functions below are identical except for the
trailing slash in the route. Flask treats these as
different routes.
"""
from flask import Flask


app = Flask(__name__)


@app.route("/hello")
def hello() -> str:
    """Return a friendly HTTP greeting."""
    return "Hello, World"


@app.route("/hello/")
def hello_slash() -> str:
    """Return another friendly HTTP greeting."""
    return "Hello, World! (with slash)"
