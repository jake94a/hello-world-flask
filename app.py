import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # html
    return f"<p>Hey demons, it's me, yah boi<p><br><p>FLASK_ENV={os.environ['FLASK_ENV']}"
