# Import dates
from datetime import date, timedelta

# Math with dates
a = 11
b = 14
l = [a,b]
# Find the least least in the list
print(min(l))

# Subtract two numbers
print(a - b)

# Add 3 to a
print(a + 3)

d1 = date(2017,11,5)
d2 = date(2017,12,4)
l = [d1,d2]

# min date
print(min(l))

# subtract two dates
delta = d2 - d1
print(delta.days) 


# Create a 29 day timedelta
td = timedelta(days=29)
print(d1+td)

"""
# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

# Put the dates in order
dates_ordered = sorted(dates_scrambled)

# Print the first and last ordered dates
print("Ordered")
print(dates_ordered[0])
print(dates_ordered[-1])
"""