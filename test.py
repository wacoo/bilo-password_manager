import sys
import os

# add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from models.base import Base, Session, engine
from models.user import User
from models.note import Notes
from models.credential import Credentials


def create_user(fname, lname, username, password):
    user = User.create(fname=fname, lname=lname, username=username, password=password)
    print(f"Created user: {user.id}, {user.fname} {user.lname}")

    return user


def create_note(title, description, upload, owner):
    note = Notes.create(title=title, description=description, upload=upload, owner=owner)
    print(f"Created note: {note.id}, {note.title}")

    return note


def create_credential(url, username, password, owner):
    credential = Credentials.create(url=url, username=username, password=password, owner=owner)
    print(f"Created credential: {credential.id}, {credential.url}")

    return credential


def update_user(user_id, **kwargs):
    user = Session().query(User).get(user_id)
    if user:
        user.update(**kwargs)
        print(f"Updated user: {user.id}, {user.fname} {user.lname}")
    else:
        print(f"User {user_id} not found")


def update_note(note_id, **kwargs):
    note = Session().query(Notes).get(note_id)
    if note:
        note.update(**kwargs)
        print(f"Updated note: {note.id}, {note.title}")
    else:
        print(f"Note {note_id} not found")


def update_credential(credential_id, **kwargs):
    credential = Session().query(Credentials).get(credential_id)
    if credential:
        credential.update(**kwargs)
        print(f"Updated credential: {credential.id}, {credential.url}")
    else:
        print(f"Credential {credential_id} not found")


def delete_user(user_id):
    user = Session().query(User).get(user_id)
    if user:
        user.delete()
        print(f"Deleted user: {user.id}, {user.fname} {user.lname}")
    else:
        print(f"User {user_id} not found")


def delete_note(note_id):
    note = Session().query(Notes).get(note_id)
    if note:
        note.delete()
        print(f"Deleted note: {note.id}, {note.title}")
    else:
        print(f"Note {note_id} not found")


def delete_credential(credential_id):
    credential = Session().query(Credentials).get(credential_id)
    if credential:
        credential.delete()
        print(f"Deleted credential: {credential.id}, {credential.url}")
    else:
        print(f"Credential {credential_id} not found")


if __name__ == '__main__':
    # create a user
    john = create_user(fname='John', lname='Doe', username='johndoe@example.com', password='password123')

    # create a note for the user
    note = create_note(title='My first note', description='This is my first note', upload=None, owner=john)

    # create a credential for the user
    credential = create_credential(url='https://example.com', username='johndoe@example.com', password='password456', owner=john)

    # update the user's first name
    update_user(user_id=john.id, fname='Jane')

    # update the note's title
    update_note(note_id=note.id, title='My updated note')

    # update the credential's username and password
    update_credential(credential_id=credential.id, username='jane@example.com', password='newpassword789')

    # delete the user
    delete_user(user_id=john.id)

    # delete the note
    delete_note(note_id=note.id)

    # delete the credential
    delete_credential(credential_id=credential.id)