import pandas as pd

# Dictionaries
my_dict = {
    "title": "Charlotte's Web",
    "author": "E. B. White",
    "published": "1952"
}

my_dict["title"]

# Creating DataFrame

# From a list of dictionaries
# # Constructed row by row
list_of_dicts = [
    {"name":"Ginger","breed":"Dachshund","height_cm":22,"weight_kg":10,"date_of_birth":"2019-03-14"},
    {"name":"Scout","breed":"Dalmatian","height_cm":59,"weight_kg":25,"date_of_birth":"2019-05-09"}
]

new_dogs = pd.DataFrame(list_of_dicts)
#print(new_dogs)


# From a dictionary of lists
# # Constructed column by column
# # key = column name
# # Value = list of column values

dict = {
    "name" : ["Ginger","Scout"],
    "breed" : ["Dachshund","Dalmatian"],
    "height_cm" : [22, 59],
    "weight_kg" : [10, 25],
    "date_of_birth" : ["2019-03-14","2019-05-09"]
}
new_dogs = pd.DataFrame(dict)