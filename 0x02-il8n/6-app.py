#!/usr/bin/env python3
"""A Flask app with prioritized locale selection based on user settings."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """Configuration for internationalization."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

def get_user(user_id: str) -> dict:
    """Retrieve a user by ID from the mock database."""
    try:
        return users.get(int(user_id))
    except (ValueError, TypeError):
        return None

@app.before_request
def before_request() -> None:
    """Set the global user before each request based on 'login_as' parameter."""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id) if user_id else None

@babel.localeselector
def get_locale() -> str:
    """Determine the best-matching locale with priority order."""
    # 1. Check URL parameter
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    # 2. Check user's preferred locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    # 3. Check request header
    header_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if header_locale:
        return header_locale
    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']

@app.route('/', strict_slashes=False)
def index() -> str:
    """Render the homepage with user-specific greetings."""
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
