# pip install sas7bdat
import pandas as pd
import matplotlib.pyplot as plt
from sas7bdat import SAS7BDAT

# SAS and Stata files (Statistical Analysis System)
# SAS: business analytics and biostatistics
# Stata: academic social science researc

with SAS7BDAT('./data/sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
# print(df_sas)

df = pd.read_stata('./data/disarea.dta')
# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()
