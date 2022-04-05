import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set() # set the seaborn style (it´s better than matplotlib style)
df = pd.read_csv("./data/bike_share.csv")


print(pd.crosstab(df["mnth"],df["weekday"],values=df["total_rentals"],aggfunc='mean').round(0)) # is frequently used to manipulate the data
# sns.heatmap(pd.crosstab(df["mnth"],df["weekday"],values=df["total_rentals"],aggfunc='mean').round(0))# function requires data to be in a grid format
df_crosstab = pd.crosstab(df["mnth"],df["weekday"],values=df["total_rentals"],aggfunc='mean').round(0)
# sns.heatmap(df_crosstab,annot=True,cmap="YlGnBu",cbar=False,linewidths=.5) # fmt="d" -> float to integer
sns.heatmap(df_crosstab,annot=True,cmap="YlGnBu",cbar=True,center=df_crosstab.loc[9,6])
# sns.heatmap(df.corr())
plt.show()