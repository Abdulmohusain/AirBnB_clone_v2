#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    """Closes the storage"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities():
    """Home page"""
    all_states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
