import pandas as pd
import numpy as np

brics = pd.read_csv("./02_Dictionaries&Pandas/data/brics.csv",index_col=0)

# print the header by DataFrame
# for val in brics:
    # print(val)


for lab , row in brics.iterrows():
    print(lab + ": " + row["capital"])

    # - Creating Series on every iteration
    # brics.loc[lab,"name_length"] = len(row["country"])
# print(brics)

brics["name_length"] = brics["country"].apply(len)
print(brics)

brics.to_csv("./02_Dictionaries&Pandas/data/brics.csv")