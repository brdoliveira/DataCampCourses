# One-to-many relationships
import pandas as pd

licenses = pd.read_pickle("./data/licenses.p")
print(licenses.head())
print(licenses.shape)

wards = pd.read_pickle("./data/ward.p")
ward_licenses = wards.merge(licenses, on="ward", suffixes=("_ward","_lic"))
print(ward_licenses.head())
