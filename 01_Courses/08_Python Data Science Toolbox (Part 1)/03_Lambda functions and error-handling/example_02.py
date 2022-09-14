# Introduction to error handling

def sqrt(x):
    """Returns the square root of a number."""
    if type(x) == int:
        if x < 0:
            raise ValueError('x must be non-negative')
    try:
        return x ** (0.5)
    except TypeError:
        print('x must be an int or float!')

sqrt(4)
sqrt(-2)
sqrt('hello')