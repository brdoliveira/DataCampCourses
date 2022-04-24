import numpy as np
import pandas as pd

marriage_status = pd.read_csv('./data/marriage_status.csv')

# Get marriage status column
marriage_status = marriage_status['marriage_status']
marriage_status.value_counts()

# Get value counts on DataFrame
marriage_status.groupby('marriage_status').count()

# Capitalize
marriage_status['marriage_status'] = marriage_status['marriage_status'].str.upper()
marriage_status['marriage_status'].value_counts()

# Lowercase
marriage_status['marriage_status'] = marriage_status['marriage_status'].str.lower()
marriage_status['marriage_status'].value_counts()

# Strip all spaces
marriage_status = marriage_status['marriage_status'].str.strip()
marriage_status['marriage_status'].value_counts()

# Using qcut()
group_names = ['0-200K','200K-500K','500K+']
marriage_status['income_group'] = pd.cut(marriage_status['household_income'], q=3, labels=group_names)

# Print income_group column
marriage_status[['income_group','household_income']]

# Using cut() = create category range and names
ranges = [0,200000,500000,np.inf]
group_names = ['0-200K','200K-500K','500K+']
marriage_status['income_group'] = pd.cut(marriage_status['household_income'], bins=ranges, labels=group_names)

# Print income_group column
marriage_status[['income_group','household_income']]



# Collapsing data into categories
devices = pd.read_csv('./data/devices.csv')
# Create mapping dictionary and replace

mapping = {'Microsoft':'DesktopOS','MacOS':'DesktopOS','Linux':'DesktopOS',
        'IOS':'MobileOS','Android':'MobileOS'}

devices['operating_system'] = devices['operating_system'].replace(mapping)
devices['operating_system'].unique()