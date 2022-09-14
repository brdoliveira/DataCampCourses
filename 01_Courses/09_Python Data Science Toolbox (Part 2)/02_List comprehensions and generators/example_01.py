# Populate a list with a for loop

nums = [12,8,21,3,16]
new_nums = []

for num in nums:
    new_nums.append(num + 1)
print(new_nums)

# A list comprehension 
new_nums = [num + 1 for num in nums]
print(new_nums)

# List comprehension with range()
result = [num for num in range(10)]
print(result)

# Nested loops
print("# # Equals")
pairs_1 = []
for num1 in range(0,2):
    for num2 in range(6,8):
        pairs_1.append((num1,num2))
print(pairs_1)

pairs_2 = [(num1,num2) for num1 in range(0,2) for num2 in range(6,8)]
print(pairs_2)