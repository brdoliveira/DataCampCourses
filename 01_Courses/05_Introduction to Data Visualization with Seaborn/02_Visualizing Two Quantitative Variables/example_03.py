from matplotlib import markers
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# subbplots (col and row)
# subgroups with color (hue)

air_df_mean = pd.read_csv("./data/air_df_mean.csv")

# Scatter plot 
sns.relplot(x="hour",y="NO_2_mean",
            data=air_df_mean,
            kind="scatter")
plt.show()

#Line plot
sns.relplot(x="hour",y="NO_2_mean",
            data=air_df_mean,
            kind="line")
plt.show()

# subgroup by location
sns.relplot(x="hour",y="NO_2_mean",
            data=air_df_mean,
            kind="line",
            style="location",
            hue="location",
            markers=True,
            dashes=False)
plt.show()

# Multiple observations
air_df = pd.read_csv("./data/air_df.csv")
sns.relplot(x="hour",y="NO_2_mean",
            data=air_df,
            kind="line",# In this case show the confidence interval
            ci="sd") # ci --> confidence interval
            # ci = None (hidden confidence interval)

plt.show()
            