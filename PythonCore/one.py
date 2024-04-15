# String declaration
my_string = "Hello, World!"

# Accessing characters in a string
print(my_string[0])  # Output: H

# Slicing a string
print(my_string[7:])  # Output: World!

# String concatenation
new_string = my_string + " Welcome!"
print(new_string)  # Output: Hello, World! Welcome!

# String methods
print(my_string.lower())  # Output: hello, world!
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.split(", "))  # Output: ['Hello', 'World!']


# List declaration
my_list = [1, 2, 3, 4, 5]

# Accessing elements in a list
print(my_list[0])  # Output: 1

# Slicing a list
print(my_list[1:3])  # Output: [2, 3]

# List concatenation
new_list = my_list + [6, 7, 8]
print(new_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# List methods
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5, 6]

print(len(my_list))  # Output: 5


import numpy as np

# Array declaration
my_array = np.array([1, 2, 3, 4, 5])

# Accessing elements in an array
print(my_array[0])  # Output: 1

# Slicing an array
print(my_array[1:3])  # Output: [2 3]

# Array concatenation
new_array = np.concatenate((my_array, np.array([6, 7, 8])))
print(new_array)  # Output: [1 2 3 4 5 6 7 8]

# Array methods
print(np.mean(my_array))  # Output: 3.0 (mean of array elements)


# Dictionary declaration
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values in a dictionary
print(my_dict['name'])  # Output: John

# Adding a new key-value pair
my_dict['gender'] = 'Male'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'gender': 'Male'}

# Dictionary methods
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city', 'gender'])
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York', 'Male'])


# Tuple declaration
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print("First element:", my_tuple[0])  # Output: 1

# Slicing
print("Sliced elements:", my_tuple[1:3])  # Output: (2, 3)

# Length of tuple
print("Length of tuple:", len(my_tuple))  # Output: 5

# Unpacking tuple
a, b, c, d, e = my_tuple
print("Unpacked elements:", a, b, c, d, e)  # Output: 1 2 3 4 5


# Set declaration
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print("Set after adding:", my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(3)
print("Set after removal:", my_set)  # Output: {1, 2, 4, 5, 6}

# Length of set
print("Length of set:", len(my_set))  # Output: 5

# Iterating through set
print("Set elements:")
for item in my_set:
    print(item)


# Dictionary declaration
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values
print("Name:", my_dict['name'])  # Output: John

# Adding a new key-value pair
my_dict['gender'] = 'Male'
print("Dictionary after adding a new key-value pair:", my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'gender': 'Male'}

# Removing a key-value pair
del my_dict['age']
print("Dictionary after removing a key-value pair:", my_dict)  # Output: {'name': 'John', 'city': 'New York', 'gender': 'Male'}

# Length of dictionary
print("Length of dictionary:", len(my_dict))  # Output: 3

# Iterating through dictionary
print("Dictionary elements:")
for key, value in my_dict.items():
    print(key, ":", value)



# If statement
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# For loop
for i in range(5):
    print(i)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1
