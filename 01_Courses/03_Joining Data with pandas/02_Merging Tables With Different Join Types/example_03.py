# Merging a table to itself
# used in graph data
import pandas as pd

sequels = pd.read_pickle('./data/sequels.p')
print(sequels.head())

# merge(left join + right join) = table result
original_sequels = sequels.merge(sequels, left_on='sequel', right_on='id',
                                suffixes=('_org','_seq')) 
print(original_sequels.head())

# Continue format results
print(original_sequels[['title_org','title_seq']].head())

original_sequels = sequels.merge(sequels, left_on='sequel', right_on='id',
                                how='left',suffixes=('_org','_seq')) 
print(original_sequels.head())