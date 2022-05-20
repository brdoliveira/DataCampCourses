# Logistic Regression --> Binary fact
import statsmodels.formula.api as smf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

gss = pd.read_hdf('./data/gss.hdf5','gss')

grouped = gss.groupby('age')
mean_income_by_age = grouped['realinc'].mean()

gss['age2'] = gss['age'] ** 2
gss['educ2'] = gss['educ'] ** 2

formula = 'realinc ~ educ + educ2 + age + age2 + C(sex)'
results = smf.ols(formula,data=gss).fit()
# print(results.params)

print("After: \n",gss['gunlaw'].value_counts()) # 1 = yes | 2 = no
gss['gunlaw'].replace([2],[0],inplace=True)
print("Before: \n",gss['gunlaw'].value_counts()) # 1 = yes | 2 = no


formula = 'gunlaw ~ educ + educ2 + age + age2 + C(sex)'
results = smf.logit(formula,data=gss).fit()
# print(results.params)

df = pd.DataFrame()
df['age'] = np.linspace(18,89)
df['educ'] = 12

df['age2'] = df['age'] ** 2
df['educ2'] = df['educ'] ** 2

df['sex'] = 1
pred1 = results.predict(df)

df['sex'] = 2
pred2 = results.predict(df)

grouped = gss.groupby('age')
favor_by_age = grouped['gunlaw'].mean()

plt.plot(favor_by_age,'o',alpha=0.5)
plt.plot(df['age'],pred1,label='Male')
plt.plot(df['age'],pred2,label='Female')

plt.xlabel('Age')
plt.ylabel('Probability of favoring gun law')
plt.legend()

plt.show()