#from models import User
from models import Credential, Note, User 
from models.base import session, Base
import datetime

if __name__ == '__main__':
    # Insert a new user
    new_user = User(fname='John', lname='Doe', email='johndoe@example.com', password='password')
    session.add(new_user)
    session.commit()

    '''# Update an existing user
    user = session.query(User).filter_by(email='johndoe@example.com').first()
    user.password = 'new_password'
    user.updated_at = datetime.datetime.now()
    session.commit()

    # Delete an existing user
    user = session.query(User).filter_by(email='johndoe@example.com').first()
    session.delete(user)
    session.commit()

    # Close the session
    session.close()
'''