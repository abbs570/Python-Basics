# Python format method called fstring

first_name = 'Abbey'
last_name = 'Noyes'

# sentence = 'My name is {} {}'.format(first_name, last_name)
# print(sentence)

# fstring example
# Run funtions or methods directly into f string
sentence = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)


person = {'name': 'Abbey', 'age' : 24}
sentence = f"My name is {person['name']} and I am {person['age']} years old"
print(sentence)

# fstring calulations
calculation = f'4 times 11 is equal to {4*11}'
print(calculation)


# 0 pad with digits
for n in range(1,11):
    sentence = f'The value is {n:02}'
    print(sentence)

# floating point values
pi = 3.14159265
sentence = f'Pi is equal to {pi:.4f}'
print(sentence)

# formatting and printing datea
from datetime import datetime

birthday = datetime(1990, 1, 1)

sentence =  f'Abbey has a birthday on {birthday:%B %d,%Y}'
print(sentence)