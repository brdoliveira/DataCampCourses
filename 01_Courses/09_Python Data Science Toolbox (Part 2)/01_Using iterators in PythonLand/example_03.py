import pandas as pd
result = []

for chunk in pd.read_csv('./data/world_ind_pop_data.csv', chunksize=1000):
    result.append(chunk['CountryName'])

# print(result)
total = len(result)
print(total)