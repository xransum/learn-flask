"""Runner module for testing the application.

The app is initialized in '__init__.py'.
"""
from . import app


def main() -> None:
    """App runner function."""
    app.run(debug=True)


if __name__ == "__main__":
    main()
