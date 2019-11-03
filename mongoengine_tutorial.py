from mongoengine import *
from datetime import datetime
import os
import json
from settingSecret import MyMongoDBServerTest01

# CONNECT TO MONGODB
result = connect(host=MyMongoDBServerTest01.hostURI)


# DEFINING DOCUMENT
class User(Document):
    description = StringField()
    username = StringField(required=True)
    password = StringField(required=True)
    email = EmailField(unique=True, required=True)
    dob = DateField()
    email_activated = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.utcnow)
    categories = ListField()
    admin = BooleanField(default=False)
    date_demo = DateField(default=datetime.today)

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
    unit = IntField()
    date_created = DateTimeField(default=datetime.utcnow)
    address = StringField(required=True)
    appointment = DateTimeField(required=True)

    meta = {
        'indexes': ['appointment'],
        'ordering': ['-date_created'],
    }


# CREATE A USER
# kim = User(username="kim", password='password', email='1234@test.com')
# kim.save()

# CREATE A BOOKING
# booking = Booking(description='Water drops', author=kim, address='Singapore', unit=4, appointment=datetime.utcnow(),
#                   parts_required=['Remote control replacement', 'Battery', 'Cleaning'])
# booking.save()

# SAVE A USER
# user1 = User('gibberish nonsense here', 'kim', 'password', '1testadmin@admin.com')
# user1.admin = True
# user1.email_activated = True
# user1.nothing = False
# user1.save()

# SAVE A BOOKING WITH NEW FIELD e.g. nothing or price
# booking1 = Booking(description='Some gibberish', address='Singapore', appointment=datetime.utcnow())
# booking1.nothing = 'Nothing here'
# booking1.price = 1.55123123143412414
# booking1.save()

# QUERY DATABASE
# users = User.objects()
# for user in users:
#     print(user.username, user.email)

# QUERY FILTER
# admins = User.objects(admin=True, email_activated=True)
# for a in admins:
#     print(a.username, a.email)

# QUERY ONLY 1 OBJECT
# try:
#     user2 = User.objects(username='xyzzkljsdlkjsdf').get()
#     print(user2.count())
#     for u in user2:
#         print(u.username)
# except:
#     print("Something went wrong!")

# QUERY BOOKING MADE BY A USER
# kim = User.objects(email='1kimm123@test.com').get()
# print("Found user:", kim.username)
# bookings_by_kim = Booking.objects(author=kim)
# for booking in bookings_by_kim:
#     print("Booking by:", booking.author.username, booking.description, booking.address, booking.appointment)

# QUERY OPERATORS contains or icontains
# users_only = User.objects(email__icontains='admin')
# for user in users_only:
#     print(user.username)

# QUERY OPERATORS (query a list)
# bookings = Booking.objects(parts_required='Battery')
# for booking in bookings:
#     print(booking.description, booking.parts_required)

# QUERY OPERATORS (query a list with multiple criteria)
# bookings = Booking.objects(parts_required__all=['Battery', 'Cleaning'])
# for booking in bookings:
#     print(booking.description, booking.parts_required)

# QUERY FIRST 2
# users = User.objects()[:2]
# for u in users:
#     print(u.username, u.date_created)

# QUERY ALL BUT FIRST 2
# users = User.objects()[2:]
# for u in users:
#     print(u.username, u.email, u.date_created)

# QUERY (FOR PAGINATION)
# users = User.objects()[2:4]
# for u in users:
#     print(u.username, u.email, u.date_created)

# COUNT
# total = User.objects().count()
# print(total)

# # COUNT WITH CRITERIA
# total = User.objects(email_activated=False).count()
# print(total)

# AGGREGATION (e.g. AVERAGE)
# average = Booking.objects.average('unit')
# print(average)

# AGGREGATION (e.g. sum)
# sum = Booking.objects.sum('unit')
# print(sum)

# RETURN JSON
# kim = User.objects(username='kim1').get()
# print(kim.json())

