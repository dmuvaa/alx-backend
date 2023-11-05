#!/usr/bin/env python3

"""import modules"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """babel config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """create a python app"""
    return render_template('1-index.html')

if __name__ == '__main__':
    """main"""
    app.run(debug=True)
