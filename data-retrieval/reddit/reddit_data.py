import os
import praw

reddit = praw.Reddit(client_id=os.environ.get("REDDIT_CLIENT_ID"),
                     client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
                     user_agent='python_server:redditnlpanalyze:v1.0')

def subreddit_comments(subreddit_name='all', comment_limit=50):
    comments = reddit.subreddit(subreddit_name).comments(limit=comment_limit)
    all_comments = ''
    for comment in comments:
        all_comments += comment.body
    return all_comments
