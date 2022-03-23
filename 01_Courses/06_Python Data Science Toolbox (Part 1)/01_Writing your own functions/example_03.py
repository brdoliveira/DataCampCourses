# Bringing it all together
def raise_both(value1,value2):
	""" Raise value1 to the power of value2 and vice versa."""
	new_value1 = value1 ** value2
	new_value2 = value2 ** value1
	
	new_tuple = (new_value1,new_value2)
	
	return new_tuple

####

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)
