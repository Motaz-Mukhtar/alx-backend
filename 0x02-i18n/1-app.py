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
    """
    LANGUAGES = ["en", "fr"]


app.config["BABEL_DEFAULT_LOCAL"] = Config.LANGUAGES[0]
app.config["BABEL_DEFAULT_TIMEZONE"] = 'UTC'


@app.route('/')
def home():
    """
        render 0-index.html template.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
