from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from flask import Flask, request, Blueprint
from flask_cors import CORS
import json
from reddit.router import router as reddit_router

app = Flask(__name__)
CORS(app)

def has_all_envs(envs):
    for env in envs:
        if not os.environ.get(env):
            return False
    return True

def no_creds(cred_src):
    no_creds_bp = Blueprint('no_creds', __name__)
    @no_creds_bp.route('/<path:path>', methods=['POST'])
    def no_creds_route(path):
        return 'The credentials for ' + cred_src + ' have not benn provided'
    return no_creds_bp

if has_all_envs(['REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET']):
    app.register_blueprint(reddit_router, url_prefix='/reddit')
else:
    app.register_blueprint(no_creds('reddit'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
