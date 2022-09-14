import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd
# Multiple regression

gss = pd.read_hdf('./data/gss.hdf5','gss')

results = smf.ols('realinc ~ educ + age',data=gss).fit()
print(results.params)

grouped = gss.groupby('age')
mean_income_by_age = grouped['realinc'].mean()

plt.plot(mean_income_by_age,'o',alpha=0.5)
plt.xlabel('Age (years)')
plt.ylabel('Income (1986 $)')

plt.show()

gss['age2'] = gss['age'] ** 2
model = smf.ols('realinc ~ educ + age + age2')
results = model.fit()
print(results.params)