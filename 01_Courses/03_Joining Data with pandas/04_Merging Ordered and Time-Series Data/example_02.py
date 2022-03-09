# Using merge_asof()
# # Similar to a merge_ordered() left join
import pandas as pd

visa = pd.read_csv("./data/visa.csv")

imb = pd.read_csv("./data/ibm.csv")

# merge_asof()
pd.merge_asof(visa,ibm, on="date_time",
	suffixes=("_visa","_ibm"))

pd.merge_asof(visa,ibm,on=['date_time'],
	suffixes=('_visa','_ibm'),
	direction='foward')

# When to use merge_asof()?
# # Data sampled from a process
# # Developing a training set (no data leakage)

# merge_asof() nearesr
# import pandas as pd
# import matplotlib as plt
# jpm_wells = pd.merge_asof(jpm, wells, on='date_time', suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
# jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', 
# suffixes=('_jpm', '_bac'), direction='nearest')
