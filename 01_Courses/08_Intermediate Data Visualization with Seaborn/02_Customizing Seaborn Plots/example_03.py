import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("wines.csv")

fig ,ax = plt.subplots()
sns.distplotdf(df['Tuition'],ax=ax)
ax.set(xlabel="Tuition 2013-14",
       ylabel="Distribuition",
       xlim=(0,50000),
       title="2013-14 Tuition and Fees Distribuition")

# Combining plots
fig, (ax0,ax1) = plt.subplots(
    nrows=1,ncols=2,sharey=True,figsize=(7,4))

sns.distplot(df['Tuition'],ax=ax0)
sns.distplot(df.query(
    'State == "MN'
)['Tuition'],ax=ax1)

ax1.set(xlabel="Tuition (MN)",xlim=(0,70000))
ax1.axvline(x=20000,label='My Budget',linestyle='--')
ax1.legend()

plt.show()