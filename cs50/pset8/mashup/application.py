import os
import re
from flask import Flask, jsonify, render_template, request, url_for
from flask_jsglue import JSGlue

from cs50 import SQL
from helpers import lookup

# configure application
app = Flask(__name__)
JSGlue(app)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///mashup.db")

@app.route("/")
def index():
    """Render map."""
    if not os.environ.get("API_KEY"):
        raise RuntimeError("API_KEY not set")
    return render_template("index.html", key=os.environ.get("API_KEY"))

@app.route("/articles")
def articles():
    """Look up articles for geo."""
    if not request.args.get("geo"):
        raise RuntimeError("there are no articles for this location")
    else:
        articles = lookup(request.args.get("geo"))
    
    # Ultimately, we’ll parse RSS feeds from Google News using Python and then return articles' titles and links to our web app via Ajax as JSON. 
    # TODO - need to return an array of objects where each object is a different article from Google News'
    # See http://flask.pocoo.org/docs/0.12/api/#module-flask.json for documentation on jsonify
    return jsonify(articles)

@app.route("/search")
def search():
    """Search for places that match query."""
    
    if not request.args.get("q"):
        raise RuntimeError("sorry can't find that location!")
        
    location = request.args.get("q") + "%"

    # TODO - need to query the database for the postal code, city, or state defined by the argument "q"
    currentPlace = db.execute("SELECT * FROM places WHERE postal_code LIKE :location OR admin_name1 LIKE :location OR\
    place_name LIKE :location", location=location)
    
    # Each row of the database table "places" is an object (ex: http://pset8.cs50.net/search?q=02138), but not necessarily 
    # in this json format yet.
    return jsonify(currentPlace)

@app.route("/update")
def update():
    """Find up to 10 places within view."""

    # ensure parameters are present
    # request.args finds the arguments in a query string after the "?="  
    # ex: request.args.get("geo") will get the word by word value of geo, and return as a string.  If there is no argument, 
    # request.args.get("geo") returns False
    if not request.args.get("sw"):
        raise RuntimeError("missing sw")
    if not request.args.get("ne"):
        raise RuntimeError("missing ne")

    # ensure parameters are in lat,lng format
    if not re.search("^-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?$", request.args.get("sw")):
        raise RuntimeError("invalid sw")
    if not re.search("^-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?$", request.args.get("ne")):
        raise RuntimeError("invalid ne")

    # explode southwest corner into two variables
    (sw_lat, sw_lng) = [float(s) for s in request.args.get("sw").split(",")]

    # explode northeast corner into two variables
    (ne_lat, ne_lng) = [float(s) for s in request.args.get("ne").split(",")]

    # find 10 cities within view, pseudorandomly chosen if more within view
    if (sw_lng <= ne_lng):

        # doesn't cross the antimeridian
        rows = db.execute("""SELECT * FROM places
            WHERE :sw_lat <= latitude AND latitude <= :ne_lat AND (:sw_lng <= longitude AND longitude <= :ne_lng)
            GROUP BY country_code, place_name, admin_code1
            ORDER BY RANDOM()
            LIMIT 10""",
            sw_lat=sw_lat, ne_lat=ne_lat, sw_lng=sw_lng, ne_lng=ne_lng)

    else:

        # crosses the antimeridian
        rows = db.execute("""SELECT * FROM places
            WHERE :sw_lat <= latitude AND latitude <= :ne_lat AND (:sw_lng <= longitude OR longitude <= :ne_lng)
            GROUP BY country_code, place_name, admin_code1
            ORDER BY RANDOM()
            LIMIT 10""",
            sw_lat=sw_lat, ne_lat=ne_lat, sw_lng=sw_lng, ne_lng=ne_lng)

    # output places as JSON
    return jsonify(rows)
