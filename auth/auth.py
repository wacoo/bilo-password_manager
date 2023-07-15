import functools
import jwt 
import uuid
from flask import request, jsonify, current_app

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
        current_app.redis_client.set(token, email)
        current_app.redis_client.expire(token, 3600) # token expires in 1 hour
        return token

    def validate_token(self, token):
        user_id = current_app.redis_client.get(token)
        if user_id:
            return user_id.decode('utf-8')
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

            return f(user_id, *args, **kwargs)

        return decorated