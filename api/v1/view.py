from flask import Blueprint, jsonify, request, current_app
from models.base import session
from models.users import User
from models.credentials import Credential
from models.notes import Note
from auth.auth import TokenAuth

view = Blueprint('view', __name__)
auth = TokenAuth()

@view.route('/', methods=['GET', 'POST'])
#@auth.requires_token
def home():
    ''' Bilo Password Manager home page '''
    email = 'wabaham9@gmail.com'#request.json.get("email")
    with current_app.app_context():
      cred_lst = {}
      note_lst = {}
      user_data = {}
      account = {}
      cred_collection = []
      note_collection = []
      notes = session.query(Note).filter_by(user_email=email).all()
      creds = session.query(Credential).filter_by(user_email=email).all()
      #user_data['credentials'] = creds
      #user_data['notes'] = notes
      for cred in creds:
         cred_lst['url'] = cred.__dict__['url']
         cred_lst['username'] = cred.__dict__['username']
         cred_lst['password'] = cred.__dict__['password']
         cred_lst['auto_fill'] = cred.__dict__['auto_fill']
         cred_lst['created_at'] = str(cred.__dict__['created_at'])
         cred_lst['updated_at'] = str(cred.__dict__['updated_at'])
         cred_lst['user_email'] = str(cred.__dict__['user_email'])
         cred_collection.append(cred_lst)
         cred_lst = {}
      user_data['credentials'] = cred_collection
      for note in notes:
         note_lst['id'] = note.__dict__['id']
         note_lst['description'] = note.__dict__['description']
         note_lst['created_at'] = str(note.__dict__['created_at'])
         note_lst['updated_at'] = str(note.__dict__['updated_at'])
         note_collection.append(note_lst)
         note_lst = {}
      user_data['notes'] = note_collection
      return jsonify(user_data)