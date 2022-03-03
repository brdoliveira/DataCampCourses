import pandas as pd

dogs = pd.read_csv("./data/dogs.csv")

dogs.to_csv("./data/dogs.csv")