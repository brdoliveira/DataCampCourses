import pandas as pd

dogs = pd.read_csv("./data/dogs.csv")

breeds = dogs["breed"] 
breeds[2:5] # 2 to 4 (5 is exclusive)
breeds[:3] # 0 to 2
breeds[:] # all

dogs_srt = dogs.set_index(["breed","color"]).sort_index()
print(dogs_srt)

dogs_srt.loc["Chow Chow":"Poodle"] # The final value "Poodle" is included

# Slicing the inner index levels badly
# dogs_srt.loc["Tan":"Grey"] # breed and color (does not work)

# Slicing the inner index levels badly 
dogs_srt.loc[
    ("Labrador","Brown"):("Schnauzer","Grey")]

# Slicing columns
dogs_srt.loc[:,"name":"height_cm"]

# Slice twice
dogs_srt.loc[
    ("Labrador","Brown"):("Schnauzer","Grey"),
    "name":"heigth_cm"]

# Dog days
dogs_d = dogs.set_index("date_of_birth").sort_index()
print(dogs_d)

# Slicing by date
# Get dogs with date_of_birth between 2014-08-25 and 2016-09-16
dogs.loc["2014-08-25":"2016-09-16"]

# Slicing by partial dates
dogs.loc["2014":"2016"]

# Subsetting by row/column number
print(dogs.iloc[2:5, 1:4])