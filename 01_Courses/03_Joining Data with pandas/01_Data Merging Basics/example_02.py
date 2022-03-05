# One-to-many relationships
import pandas as pd

licenses = pd.read_csv("./data/Bussines_Licenses.csv")
print(licenses.head())
print(licenses.shape)

wards = pd.read_csv("./data/Ward_Offices.csv")
ward_licenses = wards.merge(licenses, on="ward", suffixes=("_ward","_lic"))
print(ward_licenses.head())
