#!/usr/bin/env python3
"""
    Setup Flask app,
    and instantiate the Babel object.
"""
from flask import Flask
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
        configure the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route('/')
def home() -> str:
    """
        render 0-index.html template.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
