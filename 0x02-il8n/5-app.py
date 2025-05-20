#!/usr/bin/env python3
"""A Flask app with user login emulation and internationalization."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

def get_user(user_id: str) -> dict:
    """Retrieve a user dictionary by ID."""
    try:
        return users.get(int(user_id))
    except (ValueError, TypeError):
        return None

@app.before_request
def before_request() -> None:
    """Execute before all other functions to set the global user."""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id) if user_id else None

@babel.localeselector
def get_locale() -> str:
    """Determine the best-matching locale for the user."""
    # Check URL parameter
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Check user's preferred locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    # Fallback to browser's language settings
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index() -> str:
    """Render the homepage with user login status."""
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)