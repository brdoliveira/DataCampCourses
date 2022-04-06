# Categorical Plots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats

sns.set() # set the seaborn style (it´s better than matplotlib style)
df = pd.read_csv("data.csv")

# Basic JointGrid
g = sns.JointGrid(data=df,x="Tuition",y="ADM_RATE_ALL")
g.plot(sns.regplot,sns.displot)

# Advanced JointGrid
g = sns.JointGrid(data=df,x="Tuition",y="ADM_RATE_ALL")
g = g.plot_joint(sns.kdeplot)
g = g.plot_marginals(sns.kdeplot, shade=True)
g = g.annotate(stats.pearsonr)

# jointplot()
sns.jointplot(data=df,x="Tuition",y="ADM_RATE_ALL", kind='hex')

# Customizing a jointplot
g = (sns.jointplot(x="Tuition",
                   y="ADM_RATE_ALL",
                   kind='scatter',
                   xlim=(0,25000),
                   marginal_kws=dict(bins=15,rug=True),
                   data=df.query('UG < 2500 & Ownership == "Public')).plot_joint(sns.kdeplot)) # kind="resid"
"""
# Create a jointplot of temp vs. casual riders
# Include a kdeplot over the scatter plot
g = (sns.jointplot(x="temp",
             y="casual",
             kind='scatter',
             data=df,
             marginal_kws=dict(bins=10, rug=True))
    .plot_joint(sns.kdeplot))
    
plt.show()
plt.clf()
"""