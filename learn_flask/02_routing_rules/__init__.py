"""Flask Routing Argument Rules.

When it comes to URL paths, sometimes you will require user-provided values.
This can be done using routing variables, specified by a leading '<', a trailing
'>', and a variable name between. For example '<variable-name>', will be
passed to your routes function as 'def some_route(variable_name):'. It also
allows for type hinting for your variables, so '<int:variable-name>' will expect
the user to pass an integer as the variable.

Other types:
- string: (default) accepts any text without a slash
- int: accepts positive integers
- float: accepts positive floating point values
- path: like string but also accepts slashes
- uuid: accepts UUID strings
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Returns the Index page.

    Returns:
        str: A simple greeting.
    """
    return "Index Page"


@app.route("/user/<username>")
def show_user_profile(username: str) -> str:
    """Shows the user profile for the user.

    Args:
        username (str): The username.

    Returns:
        str: The username.
    """
    return f"User {username}"


@app.route("/post/<int:post_id>")
def show_post(post_id: int) -> str:
    """Show the post with the given ID, with ID being an integer.

    Args:
        post_id (int): The post ID.

    Returns:
        str: The post ID.
    """
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath: str) -> str:
    """Show the subpath after '/path/'.

    Args:
        subpath (str): The subpath.

    Returns:
        str: The subpath.
    """
    return f"Subpath {subpath}"


@app.route("/uuid/<uuid:uuid>")
def show_uuid(uuid: str) -> str:
    """Show the UUID after '/uuid/'.

    Args:
        uuid (str): The UUID.

    Returns:
        str: The UUID.
    """
    return f"UUID {uuid}"


@app.route("/float/<float:float>")
def show_float(float: float) -> str:
    """Show the float after '/float/'.

    Args:
        float (float): The float.

    Returns:
        str: The float.
    """
    return f"Float {float}"


@app.route("/string/<string:string>")
def show_string(string: str) -> str:
    """Show the string after '/string/'.

    Args:
        string (str): The string.

    Returns:
        str: The string.
    """
    return f"String {string}"
