#!/usr/bin/env python3
"""A Flask app with configurable locale via URL parameter."""
from flask import Flask, render_template, request
from flask_babel import Babel, _

class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """Determine the best-matching locale from URL parameter or client's preferences."""
    locale_param = request.args.get('locale', '').strip()
    if locale_param in app.config['LANGUAGES']:
        return locale_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index() -> str:
    """Render the homepage with translated content."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)