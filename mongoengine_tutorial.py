from mongoengine import *

result = connect('test', host='test', port=123)
print(result)

print("Testing!")


class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    email = StringField(unique=True, required=True)
