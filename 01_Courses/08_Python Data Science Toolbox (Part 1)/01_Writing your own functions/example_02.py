# Multiple function paramaters
def raise_to_power(value1,value2):
    """Raise value1 to the power of value2."""
    new_value = value1 ** value2
    return new_value

result = raise_to_power(4,2)
print(result) # return 16

# A quick jump int tuples
even_nums = (2,4,6)
print(type(even_nums))

# Unpacking tuples
even_nums = (2,4,6)
a,b,c = even_nums
print(a,b,c)

# Acessign tuple elements
print(even_nums[1])

second_num = even_nums[1]
print(second_num)

# returning multiple values
def raise_both(value1,value2):
    """Raise value1 to the power of value2 and vice versa."""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    
    new_tuple = (new_value1,new_value2)

    return new_tuple

result = raise_both(2,3)
print(result) # return (8,9)