import functools
import jwt 
import uuid
from flask import request, jsonify, current_app
from redis import Redis

redis_client = Redis(host='127.0.0.1', port=6379, db=0)

class TokenAuth:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.secret_key = app.config["SECRET_KEY"]

    def generate_token(self, email):
        token = str(uuid.uuid4())
        redis_client.set(token, email)
        print('email', redis_client.get(token))
        redis_client.expire(token, 3600) # token expires in 1 hour
        return token

    def validate_token(self, token):
        token_only = token.split()[1]
        email = redis_client.get(token_only)
        print(token, email)
        if email:
            return email.decode('utf-8')
        else:
            return None

    def requires_token(self, f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get("Authorization")

            if not token:
                return jsonify({"message": "Missing token"}), 403

            user_id = self.validate_token(token)

            if not user_id:
                return jsonify({"message": "Invalid token"}), 403

            return f(*args, **kwargs)

        return decorated