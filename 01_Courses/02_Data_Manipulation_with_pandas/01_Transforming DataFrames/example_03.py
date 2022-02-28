import pandas as pd

dogs = pd.read_csv("./data/dogs.csv",index_col=0)
dogs["height_m"] = dogs["height_cm"] / 100
dogs["bmi"] = dogs["weight_kg"] / dogs["height_m"] ** 2
print(dogs)

print("*" * 32)
bmi_lt_100 = dogs[dogs["bmi"] < 100]
bmi_lt_100_height = bmi_lt_100.sort_values("height_cm",ascending=False)
bmi_lt_100_height[["name","height_cm","bmi"]]
print(bmi_lt_100_height)

dogs.to_csv("./data/dogs.csv")