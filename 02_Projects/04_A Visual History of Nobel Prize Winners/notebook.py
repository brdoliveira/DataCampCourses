import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

nobel = pd.read_csv("datasets/nobel.csv")

nobel.head(6)

print(len(nobel))
print(nobel['sex'].value_counts())

nobel['birth_country'].value_counts().head(10)
nobel['usa_born_winner'] = nobel["birth_country"] == "United States of America"
nobel['decade'] = (np.floor(nobel["year"] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()

prop_usa_winners.head()

sns.set()
plt.rcParams['figure.figsize'] = [11, 7]

ax = sns.lineplot(x="decade",y="usa_born_winner",data=prop_usa_winners)

ax.yaxis.set_major_formatter(PercentFormatter(1.0))

nobel['female_winner'] = nobel["sex"] == "Female"
prop_female_winners = nobel.groupby(['decade','category'], as_index=False).agg({"female_winner":"mean"})

ax = sns.lineplot(x="decade",y="female_winner",data=prop_female_winners,hue="category")

nobel_female = nobel[nobel["sex"] == "Female"]
nobel_female.nsmallest(1,"year",keep="first")

nobel.groupby("full_name").filter(lambda x: x["full_name"].count() >= 2)

nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])

nobel['age'] = nobel["year"] - nobel["birth_date"].dt.year

sns.lmplot(x="year",y="age",data=nobel)

sns.lmplot("year","age",row="category",data=nobel)

print(nobel.nlargest(1,"age"))
nobel.nsmallest(1,"age")

youngest_winner = 'Malala' 

plt.show()