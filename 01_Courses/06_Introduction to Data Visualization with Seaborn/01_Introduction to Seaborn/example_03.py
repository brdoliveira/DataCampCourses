import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = sns.load_dataset("tips")
tips.head()

# colors can be hex code, name or the first latter
hue_colors= {"Yes" : "black",
            "No" : "red"}

sns.scatterplot(x="total_bill",
                y="tip",
                data=tips,
                hue="Smoker",
                hue_order=["Yes","No"],
                palette=hue_colors) # hue -> legend in plot (automatic), but can set the order in legend
plt.show()

sns.countplot(x="smoker",
             data=tips,
             hue="sex")
plt.show()