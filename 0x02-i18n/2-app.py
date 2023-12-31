#!/usr/bin/env python3
"""
    Setup Flask app,
    and instantiate the Babel object.
"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
        configure the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('2-app.Config')


@app.route('/')
def home() -> str:
    """
        render 0-index.html template.
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """
        Determine the best match with supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
