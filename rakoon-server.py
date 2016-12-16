import os.path
from flask import Flask
app = Flask(__name__)

@app.route('/')
def rakoon(name=None):
    return render_template('index.html', name=name)
