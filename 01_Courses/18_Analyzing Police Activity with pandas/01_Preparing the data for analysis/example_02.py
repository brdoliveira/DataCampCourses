import pandas as pd

ri = pd.read_csv('./data/police.csv') # ri -> rode island
ri.drop('county_name',axis='columns',inplace=True)
ri.dropna(subset=['stop_date','stop_time'],inplace=True)

print("Datatypes DataFrame")
print(ri.dtypes)