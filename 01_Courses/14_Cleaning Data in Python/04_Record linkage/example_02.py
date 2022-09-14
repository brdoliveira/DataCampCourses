import recordlinkage
import pandas as pd


census_a = pd.read_csv("./data/census_a.csv")
census_b = pd.read_csv("./data/census_b.csv")

# Create indexing object
indexer = recordlinkage.Index()

# Generate pairs blocked on state
indexer.block('state')
pairs = indexer.index(census_a,census_b)
print(pairs)

# Create a Compare object
compare_cl = recordlinkage.Compare()

# Find exact matches for pairs of date_of_birth and state
compare_cl.exact('date_of_birth','date_of_birth',label='date_of_birth')
compare_cl.exact('state','state',label='state')

# Find similar matches for pairs of surname and address_1 using string similarity
compare_cl.string('surname','surname',threshold=0.85,label='surname')
compare_cl.string('address_1','address_1',threshold=0.85,label='address_1')

# Find matches
potential_matches = compare_cl.compute(pairs,census_a,census_b)
print(potential_matches)

# Finding the onlly pairs we want
# potential_matches[potential_matches.sum(axis=1) => 2]
