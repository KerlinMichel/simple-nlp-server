from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from flask import Flask, request
from flask_cors import CORS
import json
from reddit_data import *

app = Flask(__name__)
CORS(app)

@app.route("/reddit/comments", methods=['POST'])
def reddit_comments():
  subreddit_name = request.get_json().get('subreddit_name')
  comment_limit = request.get_json().get('comment_limit')
  return json.dumps(subreddit_comments(subreddit_name,comment_limit))

if __name__ == "__main__":
  app.run(host='0.0.0.0')
