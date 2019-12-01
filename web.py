from flask import Flask
from pynput.keyboard import Key, Listener
import sys
app = Flask(__name__)
def web():
    @app.route("/")
    def hello():
        return "Hello World!"

    while True:
        app.run()
        if Listener.key == Key.esc:
            sys.exit()