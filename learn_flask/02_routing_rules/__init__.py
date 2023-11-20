"""Flask Routing Argument Rules.

When it comes to URL paths, sometimes
you will require user-provided values.

This can be done using routing variables,
specified by a leading '<', a trailing
'>', and a variable name between.

For example '<variable-name>', will be
passed to your routes function as
'def some_route(variable_name):'.

It also allows for type hinting for your
variables, so '<int:variable-name>' will
expect the user to pass an integer as the
variable.

Other types:
- string: (default) accepts any text
    without a slash
- int: accepts positive integers
- float: accepts positive floating point
    values
- path: like string but also accepts
    slashes
- uuid: accepts UUID strings
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Returns the Index page."""
    return 'Index Page'


@app.route('/user/<username>')
def show_user_profile(username: str) -> str:
    """Shows the user profile for the user."""
    return f'User {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
    """
    Show the post with the given ID, with ID being an
    integer.
    """
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath: str) -> str:
    """Show the subpath after '/path/'."""
    return f'Subpath {subpath}'
