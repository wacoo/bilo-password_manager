#from models import User
from models import Credential, Note, User 
from models.base import session, Base
import datetime

if __name__ == '__main__':
    # Insert a new credential
    user = session.query(User).filter_by(email='johndoe@example.com').first()
    new_credential = Credential(url='https://example.com', username='johndoe', password='password', auto_fill=True, user_email=user.email)
    session.add(new_credential)
    session.commit()

    # Update an existing credential
    credential = session.query(Credential).filter_by(url='https://example.com').first()
    credential.password = 'new_password'
    credential.updated_at = datetime.datetime.now()
    session.commit()

    # Delete an existing credential
    credential = session.query(Credential).filter_by(url='https://example.com').first()
    session.delete(credential)
    session.commit()

    # Close the session
    session.close()
