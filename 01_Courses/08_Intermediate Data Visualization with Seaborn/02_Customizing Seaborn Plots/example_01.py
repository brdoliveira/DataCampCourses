import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set() # set the seaborn style (it´s better than matplotlib style)
df = pd.read_csv("wines.csv")
df['Tuition'].plot.hist()

for style in ['white','dark','whitegrid','darkgrid','ticks']:
    sns.set_style(style)
    sns.displot(df['Tuition'])
    sns.despine(left=True)
    plt.show()