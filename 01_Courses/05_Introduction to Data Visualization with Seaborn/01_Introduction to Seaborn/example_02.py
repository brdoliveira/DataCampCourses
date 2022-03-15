import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("./data/masculinity.csv",index_col=0) # data needs to be disorganized
df.head()

sns.countplot(x="how_masculine",
              data=df)
plt.show() 
