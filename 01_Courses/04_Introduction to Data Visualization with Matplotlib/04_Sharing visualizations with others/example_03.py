import pandas as pd
import matplotlib.pyplot as plt


summer_2016_medals = pd.read_csv("./data/summer2016.csv")
print(summer_2016_medals["Sport"].value_counts())

sports = summer_2016_medals["Sport"].unique()
print(sports)

fig,ax = plt.subplots()
for sport in sports:
    sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
    ax.bar(sport, sport_df["Height"].mean(),
    yerr=sport_df["Height"].std())
ax.set_ylabel("Height (cm)")
ax.set_xticklabels(sports, rotation=90)
plt.show()

# Cartopy to Geo