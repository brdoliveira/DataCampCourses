import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

airquality = pd.read_csv('./data/airquality.csv')
print(airquality)

# Return missing values
airquality.isna()

# Get summary of missigness
airquality.isna().sum()

# Visualize missingness
msno.matrix(airquality)
plt.show()

# Isolate missing and complete values aside
missing = airquality[airquality['CO2'].isna()]
complete = airquality[~airquality['CO2'].isna()]

# Describe complete DataFrame
complete.describe()

# Describe missing DataFrame()
missing.describe()

sorted_airquality = airquality.sort_values(by='Temperature')
msno.matrix(sorted_airquality)
plt.show()

# Drop missing values
airquality_dropped = airquality.dropna(subset=['C02'])
airquality.head()

# Replace fot the mean
co2_mean = airquality['CO2'].mean()
airquality_imputed = airquality.fillna({'CO2':co2_mean})
airquality_imputed.head()