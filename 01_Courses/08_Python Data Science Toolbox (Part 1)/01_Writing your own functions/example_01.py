# Built-in functions
x = str(5)
print(type(x))


# Defining a function
def square(): # <- Function header
    new_value = 4 ** 2 # <- Function body
    print(new_value)

square() # return 16


# Function parameters
def square(value):
    new_value = value ** 2
    print(new_value)

square(4) # return 16

# Return values from functions
def square(value):
    new_value = value ** 2
    return new_value

num = square(4)
print(num) # return 16

# Docstrings :
""" Docstring is this !"""