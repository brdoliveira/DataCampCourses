import pandas as pd

ri = pd.read_csv('./data/police.csv')
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)

ri['inventory'] = ri.search_type.str.contains('Inventory',na=False)
print(f'Inventory type : {ri.inventory.dtype}')
print(f'Inventory (sum) : {ri.inventory.sum()}')

print(ri.search_type.value_counts())
print('*' * 30)
print(ri.search_type.value_counts(dropna=False))

print('*' * 30)

searched = ri[ri.search_conducted == True]
print(f'Invetory mean {searched.inventory.mean()}')