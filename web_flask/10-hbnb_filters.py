#!/usr/bin/python3
"""
Flask web application for AirBnB clone filters
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the database at the end of the request."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display the main HBnB filters HTML page."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    return render_template(
                            '10-hbnb_filters.html',
                            states=states,
                            amenities=amenities
                    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
