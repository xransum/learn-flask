"""Module for the flask application.

With most websites, you can specify different paths
to make your pages more easily accessible and memorable
to you user-base.
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


if __name__ == "__main__":
   app.run(debug=True)
