#!/usr/bin/python3
"""
Flask web application to display States and Cities.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """
    Display a list of States and their Cities in HTML.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    list_of_cities = []
    for state in sorted_states:
        list_of_cities.extend(state.cities)
    sorted_cities = sorted(list_of_cities, key=lambda x: x.name)
    return render_template(
                            '8-cities_by_states.html',
                            cities=sorted_cities,
                            states=sorted_states
    )


@app.teardown_appcontext
def close_db(error):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
