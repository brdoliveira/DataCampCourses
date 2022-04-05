# Categorical Plots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set() # set the seaborn style (it´s better than matplotlib style)
df = pd.read_csv("data.csv")


# Plots of each observation 
sns.stripplot(data=df,y="DRG Definition",x="Avarage Covered Charges",jitter=True)
sns.swarmplot(data=df,y="DRG Definition",x="Average Covered Charges") # doesn't fit a lot of data

# Abstract representations
sns.boxplot(data=df,y="DRG Definition",x="Avarage Covered Charges")
sns.violinplot(data=df,y="DRG Definition",x="Avarage Covered Charges")
sns.boxenplot(data=df,y="DRG Definition",x="Avarage Covered Charges") # box + violin

# Statistical estimates
sns.barplot(data=df,y="DRG Definition",x="Avarage Covered Charges",hue="Region")
sns.pointplot(data=df,y="DRG Definition",x="Avarage Covered Charges",hue="Region")
sns.countplot(data=df,y="DRG Definition",x="Avarage Covered Charges",hue="Region")


plt.show()