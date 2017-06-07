from flask import Flask, request
from flask_cors import CORS
import json
from snlp import *

app = Flask(__name__)
CORS(app)

@app.route("/sentiment", methods=['POST'])
def sentiment_analyze():
    text = request.get_json().get('text')
    return json.dumps(sentiment(text))

@app.route("/flesch_kindcaid_grade_level", methods=['POST'])
def fk_grade_level():
    text = request.get_json().get('text')
    return json.dumps(flesch_kincaid_grade_level(text))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
