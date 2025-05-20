#!/usr/bin/env python3
"""A Flask application with internationalization support and dynamic locale selection."""
from flask import Flask, render_template, request, current_app
from flask_babel import Babel

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
    """Determine the best-matching locale based on client's accepted languages and supported locales.
    
    Returns:
        str: The best-matching language code (e.g., 'en', 'fr').
    """
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index() -> str:
    """Render the homepage template.
    
    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)