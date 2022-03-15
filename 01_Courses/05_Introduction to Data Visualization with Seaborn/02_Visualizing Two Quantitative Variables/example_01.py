import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = pd.read_csv("./data/tips.csv")
'''
# scatterplot()
sns.scatterplot(x="total_bill",
                y="tip",
                data=tips)
plt.show()
'''

# relplots() -> create subplots

sns.relplot(x="total_bill",
            y="tip",
            data=tips,
            kind="scatter",
            col="smoker", # individuals plot
            row="smoker") # 2x2 plots
            # can use col_wrap=2, 2 plot per row 
plt.show()