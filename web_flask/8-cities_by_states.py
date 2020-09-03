#!/usr/bin/python3
"""
module notes, son
"""
if __name__ == '__main__':
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route("/states_list", strict_slashes=False)
    def states_list():
        """ pulls data from storage for HTML page """
        get_states = storage.all("State")
        state_res = get_states.values()
        return render_template("7-states_list.html", state_res=state_res)

    @app.route("/cities_by_states", strict_slashes=False)
    def cit_by_state():
        """ pulls data from storage for HTML page """
        from models import storage
        get_states = storage.all("State")
        state_res = get_states.values()
        return render_template("8-cities_by_states.html", state_res=state_res)

    @app.teardown_appcontext
    def app_teardown():
        """ handles session tear down """
        storage.close()

    app.run(host="0.0.0.0", port="5000")
