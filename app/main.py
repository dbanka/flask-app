from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def send_json():
    data = json.load(open("src/static/test.json", "r"))
    return data
