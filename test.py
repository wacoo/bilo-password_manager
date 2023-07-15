from models.base import session
from models.users import User
from models.credentials import Credential
from models.notes import Note

# create a new user
user = User(fname='John', lname='Doe', email='johndoe@example.com', password='password123')
session.add(user)
session.commit()

# create a new credential for the user
credential = Credential(url='https://example.com', username='johndoe', password='secret', auto_fill=True, user_email='johndoe@example.com')
session.add(credential)
session.commit()

# create a new note for the user
note = Note(description='Example note', upload=b'example data', user_email='johndoe@example.com')
session.add(note)
session.commit()

# update the user's password
user.password = 'newpassword456'
session.commit()

# delete the credential
session.delete(credential)
session.commit()

# delete the user and all associated credentials and notes
session.delete(user)
session.commit()