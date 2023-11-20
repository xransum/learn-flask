"""Flask Routing Example Package.

With most websites, you can specify
different path to make your pages more
easily accessible and memorable to you
user-base.
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Returns the Index page."""
    return 'Index Page'


@app.route('/hello')
def hello() -> str:
    """Returns simple 'Hello, World!'."""
    return 'Hello, World!'