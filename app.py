#!/usr/bin/env python3
# This 'shebang' instructs this file to be run with python3 on our local machine.
# Shebangs must be at the very top of the file to work. https://bash.cyberciti.biz/guide/Shebang

# Now we import our needed tools.
from datetime import datetime

from flask import Flask, render_template
import requests

# Here we set a shortcut variable to the Flask app object.
app = Flask(__name__)

# We need to define some constants for use throughout our app.
# Normally in a production environment, we'd take extra steps to hide sensitive keys.
AUTH_TOKEN = '?api_key=f02124fabd1481baff85d4f9939d4881'
BASE_URL = 'https://api.themoviedb.org/3'
POPULAR_URL = '/movie/popular'

# app.route instructs our app to serve the 'index' function (called a "view"),
#   to either the root '/' url or to the '/index'
@app.route('/')
@app.route('/index')
def index():
    # Construct the current system time for display.
    # (This is helpful so the user knows when the fetched data has changed)
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    # Now we construct the popular url from the pieces.
    # This is a good pattern to follow, if we want to add other urls in the future.
    pop_url = BASE_URL + POPULAR_URL + AUTH_TOKEN
    # Use the requests lib to fetch a list of the current popular movies.
    r = requests.get(pop_url)
    # requests has a built in function for handling json formatted data.
    data = r.json()
    # Now we are going to build a list of dictionary objects, one for each movie.
    top_20 = []
    for movie in data['results']:
        top_20.append(movie)
    # Finally, we want to send the_time and top_20 to the index.html template.
    return render_template('index.html', time=the_time, top_20=top_20)

# This runs the webserver, with the debug and live reload options.
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
