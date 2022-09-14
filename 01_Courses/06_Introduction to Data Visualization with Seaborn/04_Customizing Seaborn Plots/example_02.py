import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

'''
masculinity_data = pd.read_csv("./data/masculinity_data.csv")

height =  [62,64,69,75,66,68,65,71,76,73]
weight = [120,136,148,175,137,165,154,172,200,187]

g = sns.scatterplot(x=height,y=weight)

print(f'type g = {g}') # matplotlib.axes._subplots.AxesSubplot
'''
gdp_data = pd.read_csv("./data/gdp_data.csv")

g = sns.catplot(x="Region",
                y="Birthrate",
                data=gdp_data,
                kind="box")
g.fig.suptitle("New Title",
            y=1.03)
plt.show()