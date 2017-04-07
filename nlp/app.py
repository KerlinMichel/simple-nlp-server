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

if __name__ == "__main__":
  app.run(host='0.0.0.0')
