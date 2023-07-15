from flask import Blueprint, jsonify, request
from models.base import session
from models.users import User
from models.credentials import Credential
from models.notes import Note

view = Blueprint('view', __name__)


@view.route('/')
def home():
    ''' Bilo Password Manager home page '''
    usrs = []
    creds = session.query(Note).filter_by(id=1).all()
    print(creds)
    for usr in creds:
       usrs.append(usr.__dict__['description'])
    return jsonify({'result': usrs})