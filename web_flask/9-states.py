#!/usr/bin/python3
"""
Flask web application to display States and their Cities.
"""

from flask import Flask, render_template, abort
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Display a list of all States in HTML.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template(
                            '9-states.html',
                            states=sorted_states,
                            show_cities=False
    )


@app.route('/states/<id>', strict_slashes=False)
def state_details(id):
    """
    Display details of a specific State and its Cities.
    """
    states = storage.all(State).values()

    # Simple loop to find the state with the matching id
    state = None
    for s in states:
        if s.id == id:
            state = s
            break

    if not state:
        return render_template('9-states.html', state=None, show_cities=True)

    # Assuming state.cities returns a list of City objects
    cities = sorted(state.cities, key=lambda x: x.name)
    return render_template(
                            '9-states.html', state=state,
                            cities=cities, show_cities=True
    )


@app.teardown_appcontext
def close_db(error):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
