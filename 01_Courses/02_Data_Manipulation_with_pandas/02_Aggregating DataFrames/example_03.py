import pandas as pd

dogs = pd.read_csv("./data/dogs.csv",index_col=0)


# Summaries by group
dogs[dogs["color"] == "Black"]["weight_kg"].mean()
dogs[dogs["color"] == "Brown"]["weight_kg"].mean()
dogs[dogs["color"] == "White"]["weight_kg"].mean()
dogs[dogs["color"] == "Gray"]["weight_kg"].mean()
dogs[dogs["color"] == "Tan"]["weight_kg"].mean()

# Easy method
dogs.groupby("color")["weight_kg"].mean()

# Multiple grouped summaries
dogs.groupby("color")["weight_kg"].agg([min,max,sum])

# Grouping by multiples variables
dogs.groupby(["color","breed"])["weight_kg"].mean()

# Many groups, many summaries
dogs.groupby(["color","breed"])[["weight_kg","height_cm"]].mean()