"""Flask Static Files.

Flask static files are used to render static files such as
images, CSS, and JavaScript. This is useful for creating
web pages that are dynamic and interactive. Flask static
files are written in HTML and can be used to display data
from a database, for example.
"""
import os
from flask import Flask, render_template


current_dir = os.path.dirname(os.path.realpath(__file__))  # current directory
template_dir = os.path.join(current_dir, "templates")  # template directory
static_dir = os.path.join(current_dir, "static")  # static directory

app = Flask(
    __name__,
    template_folder=template_dir,
    static_folder=static_dir,
)


@app.route("/")
def index() -> str:
    """Render HTML page.

    Returns:
        str: Rendered HTML page.
    """
    return render_template("index.html")
