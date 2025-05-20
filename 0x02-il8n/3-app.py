#!/usr/bin/env python3
"""A flask app with internationalized templates using babel."""
from flask import Flask, render_template, request
from flask_babel import Babel, _

class config:
    """Configuration class for the flask app."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """Determine the best-matching locale based on client's preferences."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index() -> str:
    """Render the internationalized homepage."""
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)