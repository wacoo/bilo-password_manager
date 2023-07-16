from models.base import session
from models.users import User
from models.credentials import Credential
from models.notes import Note

'''user2 = User(fname='Wondmagegn', lname='Chosha', email='wabaham9@gmail.com', password='pass123')
session.add(user2)
session.commit()

user3 = User(fname='Bishaw', lname='Abraham', email='aboanarges@gmail.com', password='pass321')
session.add(user3)
session.commit()'''

# create 5 credentials for wabaham9@gmail.com
credential1 = Credential(url='https://example.com/1', username='user1', password='password1', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential1)

credential2 = Credential(url='https://example.com/2', username='user2', password='password2', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential2)

credential3 = Credential(url='https://example.com/3', username='user3', password='password3', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential3)

credential4 = Credential(url='https://example.com/4', username='user4', password='password4', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential4)

credential5 = Credential(url='https://example.com/5', username='user5', password='password5', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential5)

# create 5 notes for wabaham9@gmail.com
note1 = Note(description='This is note 1', upload=b'note1.txt', user_email='wabaham9@gmail.com')
session.add(note1)

note2 = Note(description='This is note 2', upload=b'note2.txt', user_email='wabaham9@gmail.com')
session.add(note2)

note3 = Note(description='This is note 3', upload=b'note3.txt', user_email='wabaham9@gmail.com')
session.add(note3)

note4 = Note(description='This is note 4', upload=b'note4.txt', user_email='wabaham9@gmail.com')
session.add(note4)

note5 = Note(description='This is note 5', upload=b'note5.txt', user_email='wabaham9@gmail.com')
session.add(note5)

# create 5 credentials for aboanarges@gmail.com
credential6 = Credential(url='https://example.com/6', username='user6', password='password6', auto_fill=True, user_email='aboanarges@gmail.com')
session.add(credential6)

credential7 = Credential(url='https://example.com/7', username='user7', password='password7', auto_fill=True, user_email='aboanarges@gmail.com')
session.add(credential7)

credential8 = Credential(url='https://example.com/8', username='user8', password='password8', auto_fill=True, user_email='aboanarges@gmail.com')
session.add(credential8)

credential9 = Credential(url='https://example.com/9', username='user9', password='password9', auto_fill=True, user_email='aboanarges@gmail.com')
session.add(credential9)

credential10 = Credential(url='https://example.com/10', username='user10', password='password10', auto_fill=True, user_email='aboanarges@gmail.com')
session.add(credential10)

# create 5 notes for aboanarges@gmail.com
note6 = Note(description='This is note 6', upload=b'note6.txt', user_email='aboanarges@gmail.com')
session.add(note6)

note7 = Note(description='This is note 7', upload=b'note7.txt', user_email='aboanarges@gmail.com')
session.add(note7)

note8 = Note(description='This is note 8', upload=b'note8.txt', user_email='aboanarges@gmail.com')
session.add(note8)

note9 = Note(description='This is note 9', upload=b'note9.txt', user_email='aboanarges@gmail.com')
session.add(note9)

note10 = Note(description='This is note 10', upload=b'note10.txt', user_email='aboanarges@gmail.com')
session.add(note10)

session.commit()

# create 5 credentials for wabaham9@gmail.com
credential1 = Credential(url='https://example.com/1', username='user1', password='password1', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential1)

credential2 = Credential(url='https://example.com/2', username='user2', password='password2', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential2)

credential3 = Credential(url='https://example.com/3', username='user3', password='password3', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential3)

credential4 = Credential(url='https://example.com/4', username='user4', password='password4', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential4)

credential5 = Credential(url='https://example.com/5', username='user5', password='password5', auto_fill=True, user_email='wabaham9@gmail.com')
session.add(credential5)

# create 5 notes for wabaham9@gmail.com
note1 = Note(description='This is note 1', upload=b'note1.txt', user_email='wabaham9@gmail.com')
session.add(note1)

note2 = Note(description='This is note 2', upload=b'note2.txt', user_email='wabaham9@gmail.com')
session.add(note2)

note3 = Note(description='This is note 3', upload=b'note3.txt', user_email='wabaham9@gmail.com')
session.add(note3)

note4 = Note(description='This is note 4', upload=b'note4.txt', user_email='wabaham9@gmail.com')
session.add(note4)

note5 = Note(description='This is note 5', upload=b'note5.txt', user_email='wabaham9@gmail.com')
session.add(note5)

# create 5 credentials for aboanarges@gmail.com
credential6 = Credential(url='https://example.com/1', username='user1', password='password1', auto_fill=True, user_email='aboanarges@gmail.com')
session.add(credential6)

credential7 = Credential(url='https://example.com/2', username='user2', password='password2', auto_fill=True, user_email='aboanarges@gmail.com')
session.add(credential7)

credential8 = Credential(url='https://example.com/3', username='user3', password='password3', auto_fill=True, user_email='aboanarges@gmail.com')
session.add(credential8)

credential9 = Credential(url='https://example.com/4', username='user4', password='password4', auto_fill=True, user_email='aboanarges@gmail.com')
session.add(credential9)

credential10 = Credential(url='https://example.com/5', username='user5', password='password5', auto_fill=True, user_email='aboanarges@gmail.com')
session.add(credential10)

# create 5 notes for aboanarges@gmail.com
note6 = Note(description='This is note 1', upload=b'note1.txt', user_email='aboanarges@gmail.com')
session.add(note6)

note7 = Note(description='This is note 2', upload=b'note2.txt', user_email='aboanarges@gmail.com')
session.add(note7)

note8 = Note(description='This is note 3', upload=b'note3.txt', user_email='aboanarges@gmail.com')
session.add(note8)

note9 = Note(description='This is note 4', upload=b'note4.txt', user_email='aboanarges@gmail.com')
session.add(note9)

note10 = Note(description='This is note 5', upload=b'note5.txt', user_email='aboanarges@gmail.com')
session.add(note10)

session.commit()

'''u1 = session.query(User).filter_by(email='wabaham9@gmail.com').all()
u2 = session.query(User).filter_by(email='aboanarges@gmail.com').all()

for us in u1:
    session.delete(us)
for us in u2:
    session.delete(us)
session.commit()

notes = session.query(Note).all()
creds = session.query(Credential).all()

for n in notes:
    session.delete(n)
for c in creds:
    session.delete(c)
session.commit()'''