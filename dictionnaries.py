student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# Prints value, based on key
print(student['name'])

# Prints value, based on key, and returns 'None' if key doesn't exist
print('---------------')
print(student.get('name'))
print(student.get('phone'))

# Prints value based on key, returns a specific text if key doesn't exist
print('---------------')
print(student.get('phone', 'Not Found!'))

# Add item to the dictionnary
print('---------------')
student['phone'] = '0478/88.99.55'
print(student)

# Modifies value at a key
print('---------------')
student['name'] = 'Rob'
student.update({'name': 'Rob', 'age': 29, 'courses': ['Math', 'CompSci']})
print(student)

# Deletes key
print('---------------')
del student['age']
print(student)

# Pops key value (i.e. removes + return)
print('---------------')
student['age'] = 30
age = student.pop('age')
print(str(age))

# Prints length of the dictionnary (i.e. number of keys)
print('---------------')
print(len(student))

# Prints keys or values or both
print(student.keys())
print(student.values())
print('---------------')
print(student.items())

# Print keys and values
print('---------------')
for key, value in student.items():
    print(key, value)