from mongoengine import *

result = connect('test', host='test', port=123)
print(result)
