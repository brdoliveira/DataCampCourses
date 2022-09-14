# Categorical Plots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set() # set the seaborn style (it´s better than matplotlib style)
df = pd.read_csv("data.csv")

g = sns.PairGrid(df,vars=["Fair_Mrkt_Rent","Median_Income"])
g = g.map_diag(plt.hist)
g = g.map_offdiag(plt.scatter)

# pairplot is a shortcut for the PairGrid
sns.pairplot(df,vars=["Fair_Mrkt_Rent","Median_Income"],kind='reg',diag_kind='hist')
sns.pairplot(df.query('BEDRMS < 3'),vars=["Fair_Mrkt_Rent","Median_Income","UTILITY"],hue="BEDRMS",palette='husl',plot_kws={'alpha' : 0.5})