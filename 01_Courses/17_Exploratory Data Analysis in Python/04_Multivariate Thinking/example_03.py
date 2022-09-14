import statsmodels.formula.api as smf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Multiple regression

gss = pd.read_hdf('./data/gss.hdf5','gss')

grouped = gss.groupby('age')
mean_income_by_age = grouped['realinc'].mean()

gss['age2'] = gss['age'] ** 2
gss['educ2'] = gss['educ'] ** 2

model = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss)
results = model.fit()
print(results.params)

df = pd.DataFrame()
df['age'] = np.linspace(18,85)
df['age2'] = df['age'] ** 2

df['educ'] = 12
df['educ2'] = df['educ'] ** 2

pred12 = results.predict(df)

df['educ'] = 14
df['educ2'] = df['educ'] ** 2

pred14 = results.predict(df)

df['educ'] = 16
df['educ2'] = df['educ'] ** 2

pred16 = results.predict(df)

plt.plot(mean_income_by_age,'o',alpha=0.5)
plt.plot(df['age'],pred12,label="High School")
plt.plot(df['age'],pred14,label="Associate")
plt.plot(df['age'],pred16,label="Bachelor")

plt.xlabel('Age (Years)')
plt.ylabel('Income (1986 $)')
plt.legend()

plt.show()