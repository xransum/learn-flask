"""Flask HTML Escape Package.

When it comes to user-provided values
passed for routing arguments, those
arguments could potentially be unsafe,
and raising the risk of injection
attacks.

Using the `escape` function can ensure
that potentially malicious user-provided
data is not rendered as such when rendered
by the client.
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Returns the Index page."""
    return 'Index Page'


@app.route("/<name>")
def hello(name: str) -> str:
   """Return a variable that's HTML safe."""
   return f"Hello, {escape(name)}!"
