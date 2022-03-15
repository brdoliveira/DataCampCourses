import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# subbplots (col and row)
# subgroups with color (hue)

tips = pd.read_csv("./data/tips.csv")

sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter",
            size="size", # dots size
            hue="size")
# size + hue = perfect !

plt.show()

sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter",
            hue="smoker",
            style="smoker") # style for each data type 
plt.show()

# Set alpha to be between 0 and 1
sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter",
            alpha=0.4)
plt.show()   