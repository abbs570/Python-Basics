#################################################
# Lists

courses = ['History', 'Math', 'Pysics', 'Computer Science']

# Print lenght of the list
print(len(courses))

# print list
print(courses)

# Print out the location value of the list
print(courses[0])
print(courses[3])
print(courses[-1])

# Slicing
# Print a certian length of list using the indexes, prints 0 and 1 and not including 2
print(courses[0:2])
print(courses[:2])
print(courses[2:])

# Add to the list
courses.append('Art')

#Insert at a certian position
courses.insert(0,'Art')

# Add each individual item from a list ot another list
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)

# Remove a value from a list
courses.remove('Math')

# Sort Variables
courses.sort()
print(courses)

# Finding Values
print(courses.index('Education'))


# Loop through values in list

for item in courses:
    print(item)

# 
for index, course in enumerate(courses):
    print (index,course)

# Starting value is 1
for index, course in enumerate(courses):
    print(index, course)

# str version of the courses
course_str = ''.join(courses)

##################################
# Tuples
# Tuples are immutable

