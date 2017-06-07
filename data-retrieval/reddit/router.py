from flask import request, Blueprint
import json
from reddit_data import *

router = Blueprint('reddit', __name__)

@router.route('/comments', methods=['POST'])
def reddit_comments():
    subreddit_name = request.get_json().get('subreddit_name')
    comment_limit = request.get_json().get('comment_limit')
    return json.dumps(subreddit_comments(subreddit_name,comment_limit))
