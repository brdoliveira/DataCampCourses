import pandas as pd

dogs = pd.read_csv("./data/dogs.csv")

dogs_height_by_breed_vs_color = dogs.pivot_table(
    "heigth_cm","breed", columns="color"
)
print(dogs_height_by_breed_vs_color)

# .loc[] + slicing is a power combo
dogs_height_by_breed_vs_color.loc["Chow Chow":"Poodle"]
# the loc and slicing combination is ideal for subsetting pivot tables

# the axis argument
dogs_height_by_breed_vs_color.mean(axis="index")

# calculating summary stats across columns
dogs_height_by_breed_vs_color.mean(axis="columns")