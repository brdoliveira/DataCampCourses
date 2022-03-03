import pandas as pd
import matplotlib.pyplot as plt

dogs = pd.read_csv("./data/dogs.csv")
# print(dogs)

# detecting missing values
dogs.isna() # Boolean value
dogs.isna().any()

# counting missing values
dogs.isna().sum()

# plotting missing values
dogs.isna().sum().plot(kind="bar")
plt.show()

# removing missing values
dogs.dropna()

# replacing missing values
dogs.fillna(0) # change the NaN to 0.0