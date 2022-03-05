import pandas as pd
import matplotlib.pyplot as plt

licenses = pd.read_csv("./data/Bussines_Licenses.csv")
wards = pd.read_csv("./data/Ward_Offices.csv")

grants = pd.read_csv("./data/Small/_Bussines_Grant_Agreements.csv")
print(grants.head() )

# Merging multiple DataFrames
# # Theorical merge
grants_licenses = grants.merge(licenses, on="zip")
print(grants_licenses.loc[grants_licenses['business'] == "REGGIE'S BAR & GRILL",
                        ['grant','company','account','ward','business']]) # not work


# Single merge
grants.merge(licenses, on=['address','zip'])


# Merging multiple tables
grants_licenses_ward = grants.merge(licenses, on=['address','zip']) \
                             .merge(wards, on='ward', suffixes=('_bus','_ward'))
grants_licenses_ward.head()

grants_licenses_ward.groupby('ward').agg('sum').plot(kind='bar',y='grant')
plt.show()

# Merge even more...
# # Three tables:
# df1.merge(df2,on='col') \
#    .merge(dg3,on='col')

# # Four tables:
# df1.merge(df2,on='col') \
#    .merge(dg3,on='col') \
#    .merge(df4,on='col')