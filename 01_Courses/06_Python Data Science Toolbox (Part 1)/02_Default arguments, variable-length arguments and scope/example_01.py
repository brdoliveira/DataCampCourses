def square1(value):
    """Returns the square of a number"""
    new_val = value ** 2
    return new_val

square1(4)

#new_val ## -> is not accessible

# ------

new_vall = 10

def square2(value):
    """Returns the square of a number"""
    new_vall = new_vall ** 2
    return new_vall

square2(4)

# ----
new_valll = 10
def square3(value):
    """Returns the square of a number."""
    global new_valll
    new_valll = new_valll ** 2
    return new_valll

square3(100)
new_valll # -> 100