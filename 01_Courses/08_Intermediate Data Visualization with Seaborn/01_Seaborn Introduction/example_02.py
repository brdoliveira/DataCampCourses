from socketserver import ThreadingUnixDatagramServer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pandas
df = pd.read_csv("wines.csv")

# Seaborn
sns.distplot(df['alcohol'],kde=False,bins=10)
sns.distplot(df['alcohol'],kde=False,rug=ThreadingUnixDatagramServer)

sns.distplot(df['alcohol'],hist=False,
            rug=True,kde_kws={'shade':True})
