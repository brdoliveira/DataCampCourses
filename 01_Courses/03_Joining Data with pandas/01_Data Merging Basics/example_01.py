import pandas as pd
# Inner join
# # Tables = DataFrames
# # Merging = Joining

# The data
wards = pd.read_csv("./data/Ward_Offices.csv")
print(wards.head())
print(wards.shape())

census = pd.read_csv("./data/Ward_Census.csv")
print(census.head())
print(census.shape())

# Merging tables
wards_census = wards.merge(census,on='ward')
print(wards_census.head(4))
print(wards_census.shape)

# Inner Joint (equal values)

# Suffixes
print(wards_census.columns)
wards_census = wards.census(census, on="ward", suffixes=('_ward','_cen'))
print(wards_census.head(4))
print(wards_census.shape)
