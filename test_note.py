#from models import User
from models import Credential, Note, User 
from models.base import session, Base
import datetime

if __name__ == '__main__':

    # Insert a new note
    user = session.query(User).filter_by(email='johndoe@example.com').first()
    new_note = Note(title='Note 1', description='This is the first note.', upload=b'capstone.jpg', user_email=user.email)
    session.add(new_note)
    session.commit()

    # Update an existing note
    note = session.query(Note).filter_by(title='Note 1').first()
    note.description = 'This is an updated note.'
    note.upload = b'myfile_updated.pdf'
    note.updated_at = datetime.datetime.now()
    session.commit()

    '''# Delete an existing note
    note = session.query(Note).filter_by(title='Note 1').first()
    session.delete(note)
    session.commit()

    # Close the session
    session.close()'''