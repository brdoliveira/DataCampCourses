# Conditionals in comprehensions
nums_if = [num ** 2 for num in range(10) if num % 2 == 0] 
print(nums_if)

nums_else = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print(nums_else)

# Dict comprehensions 
pos_neg = {num : -num for num in range(9)}
print(pos_neg)
print(type(pos_neg))

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >=7 else "" for member in fellowship]
print(new_fellowship)

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}
print(new_fellowship)
