# Filtering pandas DataFrame
import pandas as pd
import numpy as np

brics = pd.read_csv("./02_Dictionaries&Pandas/data/brics.csv")
# print(brics)

is_huge = brics["area"] > 8 # condition in DataFrame 
print(brics[is_huge])

# EASY
print(brics[brics["area"] > 8])

print(brics[np.logical_and(brics["area"] > 8, brics["area"] < 12)])
