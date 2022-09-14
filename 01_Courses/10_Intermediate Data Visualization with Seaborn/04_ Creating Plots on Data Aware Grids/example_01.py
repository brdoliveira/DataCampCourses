# Categorical Plots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set() # set the seaborn style (it´s better than matplotlib style)
df = pd.read_csv("data.csv")

g = sns.FacetGrid(df,col="HIGHDEG")
g.map(sns.boxplot,'Tuition',order=['1','2','3','4'])

sns.factorplot(x="Tuition",data=df,col="HIGHDEG",kind='box') # The factorplot is a simpler way to use a FacetGrid for categorical data
# FacetGrid for regression
g.map(plt.scatter,'Tuition','SAT_AVG_ALL')

# lmplot --> plots scatter and regression plots on a FacetGrid
sns.lmplot(data=df,x="Tuition",y="SAT_AVG_ALL",col="HIGHDEG",fit_reg=False)
# lmplot with regression
sns.lmplot(data=df,x="Tuition",y="SAT_AVG_ALL",col="HIGHDEG",row="REGION")