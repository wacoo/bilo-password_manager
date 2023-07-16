from models.base import session
from models.users import User
from models.credentials import Credential
from models.notes import Note

# create a new user
#user = User(fname='John', lname='Doe', email='johndoe@example.com', password='password123')
#session.add(user)
#session.commit()

'''user2 = User(fname='Wondmagegn', lname='Chosha', email='wabaham9@gmail.com', password='pass123')
session.add(user2)
session.commit()

user3 = User(fname='Bishaw', lname='Abraham', email='aboanarges@gmail.com', password='pass321')
session.add(user3)
session.commit()'''

u1 = session.query(User).filter_by(email='wabaham9@gmail.com').all()
u2 = session.query(User).filter_by(email='aboanarges@gmail.com').all()

for us in u1:
    us.delete()
for us in u2:
    us.delete() 
session.commit()

# create a new credential for the user
credential = Credential(url='https://facebook.com', username='wac', password='wac123', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential)
session.commit()

# create a new note for the user
note = Note(description='This is a screenshot of my capstone project.', upload=b'capstone.jpg', user_email='wabaham9@gmail.com')
session.add(note)
session.commit()

# create a new credential for the user
credential = Credential(url='https://example.com', username='johndoe', password='secret', auto_fill=True, user_email='johndoe@example.com')
session.add(credential)
session.commit()

# create a new note for the user
note = Note(description='Example note', upload=b'example data', user_email='johndoe@example.com')
session.add(note)
session.commit()
# create a new credential for the user
credential = Credential(url='https://example.com', username='johndoe', password='secret', auto_fill=True, user_email='johndoe@example.com')
session.add(credential)
session.commit()

# create a new note for the user
note = Note(description='Example note', upload=b'example data', user_email='johndoe@example.com')
session.add(note)
session.commit()

'''
# update the user's password
user.password = 'newpassword456'
session.commit()

# delete the credential
session.delete(credential)
session.commit()

# delete the user and all associated credentials and notes
session.delete(user)
session.commit()'''