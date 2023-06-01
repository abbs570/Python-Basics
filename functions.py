###################
# functions

def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

# print the return value
# print(hello_func())

# print the uppercase value of the return function
# print(hello_func().upper)

# Pass Arguments to the Function

print(hello_func("Hi", name = 'Corey'))

# Unpacks values *
# Accept a arbitrary number of arguments **
#Postional and keword arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': '22'}
student_info(*courses, **info)