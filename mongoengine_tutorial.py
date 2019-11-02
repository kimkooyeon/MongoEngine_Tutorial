from mongoengine import *
from datetime import datetime
import os
import json
from settingSecret import MyMongoDBServerTest01

# result = connect('test', host='test', port=123)
result = connect(host=MyMongoDBServerTest01.hostURI)
print(result)


# DEFINING DOCUMENT
class User(Document):
    description = StringField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)
    email = EmailField(unique=True, required=True)
    dob = DateField()
    email_activated = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.utcnow)

    def json(self):
        user_dict = {
            'username': self.username,
            'email': self.email,
            'dob': self.dob,
            'email_activated': self.email_activated,
        }
        return json.dumps(user_dict)

    meta = {
        'indexes': ['username', 'email'],
        'ordering': ['-date_created'],
    }


# DEFINING DYNAMIC DOCUMENT
class Booking(DynamicDocument):
    author = ReferenceField(User)
    description = StringField()
    date_created = DateTimeField(default=datetime.utcnow)
    address = StringField(required=True)
    appointment = DateTimeField(required=True)

    meta = {
        'indexes': ['appointment'],
        'ordering': ['-date_created'],
    }


# CREATE A USER
kim = User(username="kim", password='password', email='kim@test.com')
# kim.save()

# CREATE A BOOKING
booking = Booking(description='Water drops', author=User, address='Singapore', appointment=datetime.utcnow())
# booking.save()