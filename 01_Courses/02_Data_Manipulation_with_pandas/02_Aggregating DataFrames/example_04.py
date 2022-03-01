import pandas as pd
import numpy as np

dogs = pd.read_csv("./data/dogs.csv",index_col=0)


# group by to pivot table (default is mean)
dogs.pivot_table(values="weight_kg",
                index="color")

# different statistics
dogs.pivot_table(values="weight_kg",
                index="color",
                aggfunc=np.median)

dogs.pivot_table(values="weight_kg",
                index="color",
                aggfunc=[np.mean,np.median])

# pivot on two variables
dogs.groupby(["color","breed"])["weight_kg"].mean()

dogs.pivot_table(values="weight_kg",
                index="color",
                columns="breed")

dogs.pivot_table(values="weight_kg",
                index="color",
                columns="breed",
                fill_value=0) # change the NaN to 0


dogs.pivot_table(values="weight_kg",
                index="color",
                columns="breed",
                fill_value=0,
                margins=True) # margin show the median