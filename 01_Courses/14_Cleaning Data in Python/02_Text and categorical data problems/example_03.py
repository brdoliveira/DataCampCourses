import pandas as pd
import numpy as np

phone = pd.read_csv('phone.csv')
print(phone.head())

# Replace "+" with "00"
phone["Phone number"] = phone['Phone number'].str.replace("+","00")
print(phone.head())

# Replace "-" with nothing
phone["Phone number"] = phone['Phone number'].str.replace("-","")
print(phone.head())

# Replace phone numbers with lower than 10 digits to NaN
digits = phone['Phone number'].str.len()
phone.loc[digits < 10,"Phone number"] = np.nan
print(phone.head())

# Find length of each row in Phone number column
sanity_check = phone["Phone number"].str.len()

# Assert minmum phone number length is 10
assert sanity_check.min() >= 10

# Assert all numbers do not have "+" or "-"
assert phone["Phone number"].str.contains("+|-").any() == False

# Replace letters with nothing
phone["Phone number"] = phone["Phone number"].str.replace(r'\D+','')
phone.head()