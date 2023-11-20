"""Basic Flask App Package

For a Flask web application, this is it at its
core and with all first beginnings, here's
a "Hello, World!".
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
   """Returns 'Hello, World!' in HTML."""
   return "<p>Hello, World!</p>"