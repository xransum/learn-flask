"""Flask HTTP Methods.

This module demonstrates how to use HTTP methods in Flask.
"""
from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Default: GET requests only.

    By default Flask routes only accept GET requests.
    """
    return "Hello, World!"


@app.route("/hello", methods=["GET"])
def hello() -> str:
    """GET requests only (explicit).

    This route only accepts GET requests, similarly to the
    index route.
    """
    return "Hello, World!"


@app.route("/world", methods=["POST"])
def world() -> str:
    """POST requests only.

    Used typically for accepting form data.
    """
    return "Hello, World!"


@app.route("/foo", methods=["PUT"])
def foo() -> str:
    """PUT requests only.

    Used typically for updating data.
    """
    return "Hello, World!"


@app.route("/bar", methods=["DELETE"])
def bar() -> str:
    """DELETE requests only.

    Used typically for deleting data.
    """
    return "Hello, World!"


@app.route("/baz", methods=["PATCH"])
def baz() -> str:
    """PATCH requests only.

    Used typically for updating data.
    """
    return "Hello, World!"


@app.route("/qux", methods=["HEAD"])
def qux() -> str:
    """HEAD requests only.

    Used typically for checking if a resource exists.
    """
    return "Hello, World!"


@app.route("/quux", methods=["OPTIONS"])
def quux() -> str:
    """OPTIONS requests only.

    Used typically for checking what methods are allowed.
    """
    return "Hello, World!"


@app.route("/corge", methods=["TRACE"])
def corge() -> str:
    """TRACE requests only.

    Used typically for debugging.
    """
    return "Hello, World!"


@app.route("/grault", methods=["CONNECT"])
def grault() -> str:
    """CONNECT requests only.

    Used typically for proxying.
    """
    return "Hello, World!"


# These variables are just for testing a simplified login
# system. Merely for demonstration purposes.
user, passwd = None, None


@app.route("/login", methods=["GET", "POST"])
def login() -> str:
    """GET and POST requests only.

    This allows for handling multiple HTTP methods with
    a single route.
    """
    global user, passwd

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # This is just a hacky way to check for non-empty
        # values in the username and password fields.
        if any(
            [arg is None or arg.strip() == "" for arg in [username, password]]
        ):
            return "Login failed."
        else:
            # This is just a hacky way to store the username
            user, passwd = username, password
            return "Login successful."
    else:
        if user is None or passwd is None:
            # A simple login form with a username and password,
            # when this is submitted it will send a POST request
            # to this same route. This is just for demonstration
            # purposes.
            return """
                <form method="POST">
                    <input type="text" name="username" placeholder="Username">
                    <input type="password" name="password" placeholder="Password">
                    <input type="submit" value="Login">
                </form>
            """
        else:
            return f"Logged in as {user}."
