import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Box plots
# # Shows the distribution of quantitative data
# # See median, spread, skewness, and outliers
# # Facilitates comparions between groups

tips = pd.read_csv("./data/tips")

g = sns.catplot(x="time",
                y="total_bill",
                data=tips,
                kind="box",
                order=["Dinner","Lunch"],
                sym="",
                whis=[0,100])
# sym --> hidden outliers 

# Changing the whiskers using `whis`
# # By default, the whiskers extend to 1.5 * the interquartile range
# # Make them extend to 2.0 * IQR: whis= 2.0
# # Show the 5th and 95th percentiles: whis=[5,95]
# # Show min and max values: whis=[0,100]

plt.show()