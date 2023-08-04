#!/usr/bin/env python3
"""
    Setup Flask app,
    and instantiate the Babel object.
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Dict
from pytz.exceptions import UnknownTimeZoneError
from zoneinfo import ZoneInfo
import pytz
from datetime import datetime


app = Flask(__name__)
babel = Babel(app)


class Config(object):
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
    return render_template('index.html',
                           timezone=get_timezone())


@babel.localeselector
def get_locale() -> str:
    """
        Determine the best match with supported languages.
    """
    locale = request.args.get('locale')
    user = get_user()

    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    elif user:
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
def before_request() -> str:
    """
        Set user data to local.
    """
    user = get_user()
    g.user = user


@babel.timezoneselector
def get_timezone() -> str:
    """
        Return user time zone.
    """
    timezone_param = request.args.get('timezone')
    user_timezone = get_user().get('timezone')
    timezone = 'UTC'

    if timezone_param is not None:
        timezone = timezone_param
    elif user_timezone is not None:
        timezone = user_timezone

    try:
        pytz.timezone(timezone)
        dt = datetime.now(tz=ZoneInfo(timezone))
        fmt = '%b %M, %Y, %X %p'
        return dt.strftime(fmt)

    except UnknownTimeZoneError:
        return 'None'


if __name__ == "__main__":
    app.run()
