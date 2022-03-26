'''
def outer(...):
    """..."""
    x = ...

    def inner(...):
        """..."""
        y = x ** 2
    return ...

def mod2plus5(x1,x2,x3):
    """Returns the remainder plus 5 of three values."""

    new_x1 = x1 % 2 + 5
    new_x2 = x2 % 2 + 5
    new_x3 = x3 % 2 + 5

    return (new_x1,new_x2,new_x3)
'''

def mod2plus5(x1,x2,x3):
    """Returns the remainder plus 5 of three values."""

    def inner(x):
        """Returns the remainder plus 5 of a value."""
        return x % 2 + 5
    
    return (inner(x1),inner(x2),inner(x3))

print(mod2plus5(1,2,3))

def raise_val(n):
    """Return the inner function."""

    def inner(x):
        """Raise x to the power of n."""
        raised = x ** n
        return raised

    return inner

square = raise_val(2)
cube = raise_val(3) # now square and cube is a function!
print(f'type cube: {type(cube)}')
print(square(2),cube(4))

# Using nonlocal
def outer():
    """Prints the value of n."""
    n=1

    def inner():
        nonlocal n
        n = 2
        print(n)

    inner()
    print(n) #  nonlocal to create and changes names in an enclosing scope.

outer()

#LEGB

# L --> Local Scope
# E --> Enclosing functions
# G --> Global
# B --> Built-in