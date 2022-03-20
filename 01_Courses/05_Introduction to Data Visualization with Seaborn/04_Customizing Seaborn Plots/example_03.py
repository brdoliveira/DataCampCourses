import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gdp_data = pd.read_csv("./data/gdp_data.csv")
 
# FacetGrid
g = sns.catplot(x="Region",
                y="Bithrate",
                data = gdp_data,
                kind="box"
)
g.fig.suptitle("New Title",
                y=1.03)

#AxesSubplot

g = sns.boxplot(x="Region",
                y="Birthrate",
                data = gdp_data)

g.set_title("New Title",
            y=1.03)

## Titles for subplots
g = sns.catplot(x="Region",
                y="Bithrate",
                data = gdp_data,
                kind="box",
                col="Group") # col = Adding subplots 

g.fig.subtitle("New Title",
            y = 1.03)

g.set_titles("This is {col_name}")

# Adding axis labels

g.set(xlabel="New X Label",
    ylabel="New Y label")

plt.xticks(rotation=90)
plt.show()