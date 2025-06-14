#!/usr/bin/env python3
""" A flask app using internatiolizan using babel."""

from flask import Flask, render_template
from flask_babel import Babel

class config:
    """Configuration class for flask babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)

@app.route('/', strict_slashes=False)
def index() -> str:
    """Render the index page.
    
    Returns:
        str: rendered HTML page.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)