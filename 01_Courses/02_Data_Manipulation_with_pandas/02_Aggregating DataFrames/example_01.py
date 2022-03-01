import pandas as pd

dogs = pd.read_csv("./data/dogs.csv",index_col=0)

dogs["height_cm"].mean() # heigth average
dogs["height_cm"].mode()
dogs["height_cm"].mode()

dogs["height_cm"].min()
dogs["height_cm"].max()

dogs["height_cm"].var()
dogs["height_cm"].std()

dogs["height_cm"].quantile() # calculate quantiles

def pct30(column):
    return column.quantile(0.3)

# individual
print(dogs["weight_kg"].agg(pct30))

# multiple
print(dogs[["weight_kg","height_cm"]].agg(pct30))

# multiple summaries
def pct40(column):
    return column.quantile(0.4)

dogs["weight_kg"].agg([pct30,pct40])

dogs["weight_kg"].cumsum() # cumulative sum
dogs["weight_kg"].cummin()
dogs["weight_kg"].cumprod()