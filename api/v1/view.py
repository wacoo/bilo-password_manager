from flask import Blueprint, jsonify, request, current_app
from models.base import session
from models.users import User
from models.credentials import Credential
from models.notes import Note
from auth.auth import TokenAuth

view = Blueprint('view', __name__)
auth = TokenAuth()

@view.route('/')
@auth.requires_token
def home():
    ''' Bilo Password Manager home page '''
    with current_app.app_context():
      usrs = []
      creds = session.query(Note).filter_by(id=1).all()
      print(creds)
      for usr in creds:
         usrs.append(usr.__dict__['description'])
      return jsonify({'result': usrs})