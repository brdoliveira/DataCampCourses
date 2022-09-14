import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from numpy import median


# Point plot
# # Point show mean of quantitative variable
# # Vertical lines show 95% confidence intervals

masculinity_data = pd.read_csv("./data/masculinity_dat")
tips = pd.read_csv("./data/tips.csv")

# Line plot: avarage level of nitrogen dioxide over time
# Point plot: avarage restaurant bill, smokers vs. non-smokers

sns.catplot(x="age",
            y="masculinity_important",
            data=masculinity_data,
            hue="feel_masculinity",
            kind="point",
            join=False)

# Displaying the median
sns.catplot(x="smoker",
            y="total_bill",
            data=tips,
            kind="point",
            estimator=median,
            capzise=0.2) # capsize customizing the confidence intervals
# ci=None --> turnoff ci
plt.show()

# Point plots vs. line plots
# # Both show:
# # # Mean of quantitative variable
# # # 95% confidence intervals for the mean 
# # Differences:
# # # Line plot has quantitative variable (usually time) on x-axis
# # # Point plot has categorical variable on x-axis