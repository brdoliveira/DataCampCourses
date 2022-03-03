import matplotlib.pyplot as plt
import pandas as pd

dogs = pd.read_csv("./data/dogs.csv")

# Histogram
dogs["height_cm"].hist(bins=5)
# dogs["height_cm"].hist(bins=20)
plt.show()

# Bar plots
avg_weight_by_breed = dogs.groupby("breed")["weight_kg"].mean()
print(avg_weight_by_breed)
avg_weight_by_breed.plot(kind="bar",
                        title="Mean Weight by dog Breed")
plt.show()

# In this case, the data is not correlated, so there is no information
# Line Plot
# dogs.plot(x="height_cm",
#           y="weight_kg",
#           kind="line",
#           rot=45) # rot = label
# plt.show()

# Scatter plots
# dogs.plot(x="height_cm",
#           y="weight_kg",
#           kind="scatter")
# plt.show()

# dog_pack[dog_pack["sex"] == "F"]["height_cm"].hist(alpha=0.7)
# dog_pack[dog_pack["sex"] == "M"]["height_cm"].hist(alpha=0.7)
# plt.legend(["F","M"])
# plt.show()