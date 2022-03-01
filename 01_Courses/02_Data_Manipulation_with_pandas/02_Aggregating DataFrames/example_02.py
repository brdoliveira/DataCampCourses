import pandas as pd

dogs = pd.read_csv("./data/dogs.csv",index_col=0)


# Drop duplicates (in this case we don't have duplicate data)
dogs.drop_duplicates(subset="name")
unique_dogs = dogs.drop_duplicates(subset=["name","breed"])

unique_dogs["breed"].value_counts()
unique_dogs["breed"].value_counts(sort=True) # in order
unique_dogs["breed"].value_counts(normalize=True) # normalize * 100 = percentage
