import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# relational plots --> relplot()
# categorical plots --> catplot()

masculinity_data = pd.read_csv("./data/masculinity_data.csv")
tips = pd.read_csv("./data/tips.csv")

sns.countplot(x="how_masculinity",
            data = masculinity_data,
            kind="count") # type is count

# Changing the order
category_order = ["No answer",
                  "Not at all",
                  "Not very",
                  "Somewhat",
                  "Very"]

sns.catplot(x="how_masculinity",
            data=masculinity_data,
            kind="count",
            order=category_order)

# Bar plots
# # Display mean of quantitative variable per category
sns.catplot(x="day",
            y="total_bill",
            data=tips,
            kind="bar")

# Confidence intervals
# #  Line show 95% confidence intervas for the mean
# # Shows uncertainty about our estimate
# # Assumes our data is a random sample
# disable ci --> ci=None

# Changing the orientation
sns.catplot(x="total_bill",
            y="day",
            data=tips,
            kind="bar")

plt.show()

