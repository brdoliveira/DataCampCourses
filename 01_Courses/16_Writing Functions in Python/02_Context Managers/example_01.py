with open('my_file.text') as my_file:
    text = my_file.read()
    length = len(text)

print('The file is {} characters long'.format(length))


"""
with <context-manager>(<args>) as <variable-name>:
    # Run your code here
    # This code is running "inside the context"

# This code runs after the context is removed
"""