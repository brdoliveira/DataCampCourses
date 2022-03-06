import pandas as pd
# Inner join
# # Tables = DataFrames
# # Merging = Joining

# The data
wards = pd.read_pickle("./data/ward.p")
print(wards.head())
print(wards.shape)
print("*" * 32)


census = pd.read_pickle("./data/census.p")
print(census)
print(census.shape)
print("*" * 32)

# Merging tables
wards_census = wards.merge(census,on='ward')
print(wards_census.head(4))
print(wards_census.shape)
print("*" * 32)

# Inner Joint (equal values)

# Suffixes
print(wards_census.columns)
wards_census = wards.merge(census, on="ward", suffixes=('_ward','_cen'))
print(wards_census.head(4))
print(wards_census.shape)
print("*" * 32)
