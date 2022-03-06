from turtle import onclick
import pandas as pd
import matplotlib.pyplot as plt

licenses = pd.read_pickle("./data/licenses.p")
# print(licenses.columns)
wards = pd.read_pickle("./data/ward.p")
# print(wards.columns)

grants = pd.read_pickle("./data/business_owners.p")
# print(grants.columns)

# Merging multiple DataFrames
# # Theorical merge
grants_licenses = wards.merge(licenses, on="zip")
# print(grants_licenses)
# print(grants_licenses.loc[grants_licenses['business'] == "REGGIE'S BAR & GRILL",
#                         ['grant','company','account','ward','business']]) # not work


# # Single merge
wards.merge(licenses, on=['address','zip'])


# # Merging multiple tables
grants_licenses_ward = wards.merge(licenses, on=['address','zip','ward']) \
                            .merge(grants, on="account")
print(grants_licenses_ward.columns)
grants_licenses_ward.groupby('ward').agg('sum').plot(kind='bar')
plt.show()

# # Merge even more...
# # # Three tables:
# # df1.merge(df2,on='col') \
# #    .merge(dg3,on='col')

# # # Four tables:
# # df1.merge(df2,on='col') \
# #    .merge(dg3,on='col') \
# #    .merge(df4,on='col')