#!/usr/bin/python3

"""
    app.py

    MediaWiki Action API Code Samples

    Nearby places viewer app: Demo of geo search for wiki pages
    near a location using the Geolocation API and MediaWiki Action
    API's Geosearch module.

    MIT license
"""

from flask import Flask, render_template, request, jsonify
import requests
from haversine import haversine

APP = Flask(__name__)
SESSION = requests.Session()
API_ENDPOINT = 'https://en.wikipedia.org/w/api.php'


@APP.route('/', methods=['GET', 'POST'])    # extend the route to handle POST requests
def index():
    """ Displays the index page accessible at '/'
    """
    if request.method == "POST":

        # obtain location data in json format from the request object
        data = request.get_json()
        latitude = data['latitude']
        longitude = data['longitude']

        # pass the location data to fetch_places_nearby() for further processing
        results = fetch_places_nearby(latitude, longitude)
        print(results)
        return jsonify(results=results)

    return render_template('places.html')


def fetch_places_nearby(lat, lon):
    """ Fetches nearby places via MediaWiki Action API's Geosearch module
    """
    params = {
        "action": "query",
        "prop": "coordinates|pageimages|description|info",
        "inprop": "url",
        "pithumbsize": 144,
        "generator": "geosearch",
        "ggsradius": 10000,
        "ggslimit": 10,
        "ggscoord": str(lat) + "|" + str(lon),
        "format": "json",
    }

    res = SESSION.get(url=API_ENDPOINT, params=params)
    data = res.json()
    print(data)
    places = data['query'] and data['query']['pages']

    # further process 'places' list
    results = []

    for k in places:
        title = places[k]['title']
        description = places[k]['description'] if "description" in places[k] else ''
        thumbnail = places[k]['thumbnail']['source'] if "thumbnail" in places[k] else ''
        article_url = places[k]['fullurl']

        cur_loc = (lat, lon)
        place_loc = (places[k]['coordinates'][0]['lat'], places[k]['coordinates'][0]['lon'])

        distance = round(haversine(cur_loc, place_loc, unit='mi'), 2)

        results.append({
            'title': title,
            'description': description,
            'thumbnail': thumbnail,
            'articleUrl': article_url,
            'distance': distance
        })

    return results


if __name__ == '__main__':
    APP.run(debug=True)
