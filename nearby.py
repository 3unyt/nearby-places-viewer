#!/usr/bin/python3

"""
    nearby.py

    MediaWiki Action API Code Samples

    Nearby places viewer app: Demo of geo search for wiki pages
    near a location using the Geolocation API and MediaWiki Action
    API's Geosearch module.

    MIT license
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('places.html')


if __name__ == '__main__':
    app.run()
