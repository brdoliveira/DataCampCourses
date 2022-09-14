import pandas as pd

height_weight = pd.read_csv("./data/height_weight.csv")
height_weight.head()

# Get duplicates across all columns
duplicates = height_weight.duplicated()
height_weight[duplicates]
print(duplicates)

# Column names to check for duplication
column_names = ['first_name','last_name','address']
duplicates = height_weight.duplicated(subset= column_names, keep=False)
height_weight[duplicates]

# Output duplicate values
height_weight[duplicates].sort_values(by='first_name')

# Drop duplicates
height_weight.drop_duplicates(inplace=True)

# Output duplicate values
column_names = ['first_name','last_name','address']
duplicates = height_weight.duplicated(subset= column_names, keep=False)
height_weight[duplicates].sort_values(by='first_name')

# Group by column names and produce statistical summaries
column_names = ['first_name','last_name','address']
summaries = {'height':'max','weight':'mean'}
height_weight = height_weight.groupby(by=column_names).agg(summaries).reset_index()

# Make sure aggregation is done
duplicates = height_weight.duplicated(subset= column_names, keep=False)
height_weight[duplicates].sort_values(by='first_name')