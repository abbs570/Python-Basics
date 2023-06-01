# Duck Typing
# EAFP - Easier to ask for forgiveness than permission

class Duck:

    def quack(self):
        print('Quack, Quack')

    def fly (self):
        print('Flap, flap')

class Person:

    def quack(self):
        print("i'm quacking like a duck")
    
    def fly(self):
        print('Im flapping my arms')

def quack_and_fly(thing):
    #not duck typed, non pythonic
    # if instance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    print('this has to  be a duck')

d = Duck()
quack_and_fly(d)

p =Person()
quack_and_fly(p)