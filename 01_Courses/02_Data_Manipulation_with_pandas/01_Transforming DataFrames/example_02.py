import pandas as pd

dogs = pd.read_csv("./data/dogs.csv",index_col=0)

# Sorting
dogs.sort_values("weight_kg")

# Sorting in descending order
dogs.sort_values("weight_kg", ascending=False)

# Sorting by multiple variables
dogs.sort_values(["weight_kg","height_cm"])

# Sorting by multiple variables (changing the ascending)
dogs.sort_values(["weight_kg","height_cm"],
                ascending=[True,False])

dogs["name"]

# Subsetting multiple columns
dogs[["breed","height_cm"]]

cols_to_subset = ["breed","height_cm"]
dogs[cols_to_subset]

dogs["height_cm"] > 50
dogs[dogs["height_cm"] > 50]

dogs[dogs["breed"] == "Labrador"]

# Subsetting based on text data
dogs[dogs["date_of_birth"] > "2015-01-01"]

# Subsetting based on multiple conditions
is_lab = dogs["breed"] == "Labrador"
is_brown = dogs["breed"] == "Brown"
dogs[is_lab & is_brown]

# If you want to filter on multiple values of a categorical variable, the easiest way is to use the 
# isin method. This takes in a list of values to filter for.
is_black_or_brown = dogs["color"].isin(["Black","Brown"])
dogs[is_black_or_brown]