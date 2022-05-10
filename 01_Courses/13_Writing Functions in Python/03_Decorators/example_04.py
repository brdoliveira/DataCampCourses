def double_args(func):
    # Define a new function that we can modify
    def wrapper(a,b):
        # For now, just call the unmodified function
        return func(a * 2,b * 2)
    # Return the new function
    return wrapper

def multiply(a,b):
    return a * b

new_multiply = double_args(multiply)
print(new_multiply(1,5))


# ------------------

def double_args(func):
    # Define a new function that we can modify
    def wrapper(a,b):
        # For now, just call the unmodified function
        return func(a * 2,b * 2)
    # Return the new function
    return wrapper

@double_args
def multiply(a,b):
    return a * b

print(multiply(1,5))