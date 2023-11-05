#!/usr/bin/env python3

"""import requests"""

from flask import Flask, render_template
from flask_babel import Babel
import requests


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ config class to set babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    """ an endpoint to the index page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
