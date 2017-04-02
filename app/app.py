from flask import Flask, request
import json
from snlp import *

app = Flask(__name__)

@app.route("/sentiment", methods=['POST'])
def sentiment_analyze():
  text = request.get_json().get('text')
  return json.dumps(sentiment(text))

if __name__ == "__main__":
  app.run(host='0.0.0.0')
