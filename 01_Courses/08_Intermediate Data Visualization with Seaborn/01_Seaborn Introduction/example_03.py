import imp
import matplotlib
from matplotlib import pyplot as plt


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/wines.csv")

sns.regplot(x="alcohol",y="pH",data=df)

sns.lmplot(x="alcohol",y="quality",data=df) # powerfull (is much more flexible)

sns.lmplot(x="quality",y="alcohol",data=df,hue="type")
sns.lmplot(x="quality",y="alcohol",data=df,hue="col")