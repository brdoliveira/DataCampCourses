# Categorical Plots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set() # set the seaborn style (it´s better than matplotlib style)
df = pd.read_csv("./data/bike_share.csv")

# No order
sns.regplot(data=df,x='temp',y='total_rentals',marker='+')
sns.residplot(data=df,x='temp',y='total_rentals') # useful for evaluating the fit of a modal
sns.regplot(data=df,x='temp',y='total_rentals',order=2) # supports polynomial regression using the order parameter
sns.residplot(data=df,x='temp',y='total_rentals',order=2)

# Categorical
sns.regplot(data=df,x='mnth',y='total_rentals',x_jitter=.1,order=2)
sns.regplot(data=df,x='mnth',y='total_rentals',x_estimator=np.mean,order=2) # x_estimator can be useful for highlighting trends
sns.regplot(data=df,x='temp',y='total_rentals',x_bins=4)
plt.show()