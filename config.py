"""Flask config."""
from os import environ, path

BASE_DIR = path.abspath(path.dirname(__file__))


class Config:
    """Flask configuration variables."""

    # General Config

    FLASK_APP = "main.py"

    # Static Assets
    STATIC_FOLDER = "static/css"
    TEMPLATES_FOLDER = "templates"

