# Import recordlinkage and generate full pairs
from multiprocessing.reduction import duplicate
import recordlinkage
import pandas as pd

indexer = recordlinkage.Index()
indexer.block('state')

census_A = pd.read_csv("./data/census_A.csv")
census_B = pd.read_csv("./data/census_B.csv")

full_pairs = indexer.index(census_A,census_B)

# Comparison step
compare_cl = recordlinkage.Compare()
compare_cl.exact('date_of_birth','date_of_birth',label='date_of_birth')
compare_cl.exact('state','state',label='state')
compare_cl.string('surname','surname',threshold=0.85,label='surname')
compare_cl.string('address_1','address_1',threshold=0.85,label='address_1')

potential_matches = compare_cl.compute(full_pairs,census_A,census_B)

matches = potential_matches[potential_matches.sum(axis=1) >= 3]
print(matches.index)

# Get indices from census_B only
duplicate_rows = matches.index.get_level_values(1)
print(duplicate_rows)

# Finding duplicates in census_B
census_B_duplicates = census_B[census_B.index.isin(duplicate_rows)]

# Finding new rows in census_B
census_B_new = census_B[~census_B_duplicates]

# Link the DataFrames!
full_census = census_A.append(census_B_new)