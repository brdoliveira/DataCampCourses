# Using merge_ordered()
import pandas as pd

# Stock data
appl = pd.read_csv('./data/stock_data.csv')

# McDonalds data
mcd = pd.read_csv('./data/mdc.csv')

pd.merge_ordered(appl,mcd,on='date',
		suffixes=('_aapl','_mcd'))

# Foward fill
pd.merge_ordered(appl,mcd,on='date',
		suffixes=('_aapl','_mcd'),
		fill_method='ffill') # Fills missing with previous value
		
# When to use merge_ordered()?
# # Ordered data/time series
# # Filling in missing values

