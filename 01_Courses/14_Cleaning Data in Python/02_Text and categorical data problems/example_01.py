'''
import pandas as pd

study_data = pd.read_csv('./data/study.csv')
print(study_data.head())

categories = pd.read_csv('./data/categories.csv')
print(categories)

inconsistent_categories = set(study_data['blood_type']).difference(categories['blood_type'])
print(inconsistent_categories)

# Get and print rows with inconsistent categories
inconsistent_rows = study_data['blood_type'].isin(inconsistent_categories)
print(study_data[inconsistent_rows])

# Drop inconsistent categories and get consistent data only
consistent_data = study_data[~inconsistent_rows] # return except row
'''
