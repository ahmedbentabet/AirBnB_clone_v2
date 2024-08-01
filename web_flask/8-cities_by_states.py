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
    organized_data = []

    # Loop through states, sorted by name
    for state in sorted(states, key=lambda x: x.name):
        # Create a dictionary for each state
        state_data = {
            'name': state.name,
            'id': state.id,
            # List of cities, sorted by name
            'cities': sorted(state.cities, key=lambda x: x.name)
        }
        # Add state data to the organized_data list
        organized_data.append(state_data)

    return render_template('8-cities_by_states.html', states=organized_data)


@app.teardown_appcontext
def close_db(error):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
