#!/usr/bin/env python3
"""
    Setup Flask app,
    and instantiate the Babel object.
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Dict


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
        configure the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('6-app.Config')


@app.route('/')
def home() -> str:
    """
        render 0-index.html template.
    """
    print(g.user)
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> str:
    """
        Determine the best match with supported languages.
    """
    locale = request.args.get('locale')
    user = get_user()

    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    elif user.get('locale'):
        if user.get('locale') in app.config['LANGUAGES']:
            return get_user().get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict:
    """
        Return user dictionary or None if the
        ID cannot be found, or if login_as was
        not passed.
    """
    user_id = request.args.get('login_as')
    if not user_id:
        return None

    user_id = int(user_id)
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """
        Set user data to local.
    """
    user = get_user()
    g.user = user


if __name__ == "__main__":
    app.run()
