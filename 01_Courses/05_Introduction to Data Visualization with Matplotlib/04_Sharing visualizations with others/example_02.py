import pandas as pd
import matplotlib.pyplot as plt

medals = pd.read_csv('./data/medals_by_country_2016.csv')
fig , ax = plt.subplots()

ax.bar(medals.index,medals["Gold"])
ax.set_xticklabels(labels=medals.index,rotation=90) # rotation the label
ax.set_ylabel("Number of medals")

# Size
fig.set_size_inches([5,3])
fig.set_size_inches([3,5])

fig.savefig("gold_medals.png")

# Different file formats
fig.savefig("gold_medals.jpg")
fig.savefig("gold_medals.jpg", quality=50)
fig.savefig("gold_medals.svg")

# Resolution
fig.savefig("gold_medals.png",dpi=300)
