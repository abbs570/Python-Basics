# LEGB
'''
Local, Enclosing, Global, and Built In
Order that determines what a variable is assigned to
'''
# # use built ins scope
# import builtins
# # print (dir(builtins))
# # A global variable bc it is in the main body of the file
# x = 'global x'
# m = min([5,6,3,2,7])
# print (m)

# def my_min():
#     pass

# def test(z):
#     # global x 
#     x = 'local x'
#     print(z)

# test('local z')
# # print(z)



# Enclosing

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

