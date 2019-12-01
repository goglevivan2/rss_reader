from flask import Flask,render_template
from pynput.keyboard import Key, Listener
import sys
app = Flask(__name__)
def web(infoDic):
    @app.route("/")
    def hello():
        return render_template('index.html',dict=infoDic.values())

    while True:
        app.run()
        if Listener.key == Key.esc:
            sys.exit()