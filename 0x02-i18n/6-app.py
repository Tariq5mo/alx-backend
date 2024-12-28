#!/usr/bin/env python3
"""Flask app
"""
from typing import Dict, Union
from flask import Flask, g, render_template, request
from flask_babel import Babel


class Config:
    """The configuration for the Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


def get_user() -> Union[None, Dict[str, str]]:
    """

    Returns:
        _type_: _description_
    """
    try:
        user_id = int(request.args.get('login_as'))
        if user_id is not None and user_id in users.keys():
            return users[user_id]
        return None
    except Exception:
        return None


@babel.localeselector
def get_locale():
    """The best match for the supported languages

    Returns:
        str: The best match for the supported languages
    """
    try:
        lang = request.args.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
        lang = g.user['locale']
        if lang in app.config['LANGUAGES']:
            return lang
        lang = request.headers.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    except Exception:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """

    Returns:
        _type_: _description_
    """
    user_dict = get_user()
    g.user = user_dict


@app.route('/')
def home():
    """Home page
    """
    return render_template('5-index.html', user=g.user)


if __name__ == '__main__':
    app.run(debug=True)
