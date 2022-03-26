# Add a default argument
def power(number ,pow=1):
    """Raise number to the power of pow."""
    new_value = number ** pow
    return new_value

power(9,2)

power(9,1)

power(9)

# Flexible arguments: *args(1)
def add_all(*args):
    """Sum all values in *args together"""

    # Initialine sum
    sum_all = 0

    # Accumulate the sum
    for num in args:
        sum_all += num
    
    return sum_all

add_all(1)
add_all(2,35)
add_all(20,34,20,4)
add_all(1,2,3,4,5,6,203)

def print_all(**kwargs):
    """Print oout key-value pairs in **kwargs"""

    # Print out the key-value pais
    for key,value in kwargs.items():
        print(key + ":" + value)

print_all(name="dumbledore", job="headmaster")