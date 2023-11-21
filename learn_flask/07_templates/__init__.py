"""Flask Templates.

Flask templates are used to render HTML pages. This is
useful for creating web pages that are dynamic and
interactive. Flask templates are written in HTML and
can be used to display data from a database, for
example.
"""
import os
from flask import Flask, render_template


current_dir = os.path.dirname(os.path.realpath(__file__))  # current directory
template_dir = os.path.join(current_dir, "templates")  # template directory

app = Flask(
    __name__,
    template_folder=template_dir,
)


@app.route("/")
def index() -> str:
    """Render HTML page.

    Returns:
        str: Rendered HTML page.
    """
    return render_template("index.html")


@app.route("/hello")
def hello() -> str:
    """Render HTML page.

    Returns:
        str: Rendered HTML page.
    """
    return render_template("hello.html")
