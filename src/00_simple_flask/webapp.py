"""Module for the flask application."""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
   """Returns Hello, World! in html."""
   return "<p>Hello, World!</p>"


if __name__ == "__main__":
   app.run(debug=True)
