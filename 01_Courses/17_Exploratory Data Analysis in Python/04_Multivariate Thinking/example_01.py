import statsmodels.formula.api as smf
import pandas as pd
# Multiple regression

brfss = pd.read_hdf('./data/brfss.hdf5','brfss')
results = smf.ols('INCOME2 ~ _VEGESU1', data=brfss).fit() # ols = ordinary list squares
print(results.params)