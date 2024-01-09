#!/usr/bin/env python3
"""2. get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class for flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get user locale from flask request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
