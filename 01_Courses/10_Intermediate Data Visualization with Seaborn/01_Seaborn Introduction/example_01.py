import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pandas
df = pd.read_csv("wines.csv")

# Matplotlib
fig , ax = plt.subplots()
ax.hist(['alcohol'])

df['alcohol'].plot.hist()

# Seaborn
sns.distplot(df['alcohol'])

