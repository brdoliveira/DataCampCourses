"""
# Correlation caveats
import numpy as np

# Correlation only accounts for linear relationship
# # Correlation shouln't be used blindly 
df['x'].corr(df['y'])

# Log transformation
msleep['log_bodywt'] = np.log(msleep['bodywt'])

sns.lmplot(x='log_bodywt',
           y='awake',
           data=msleep,
           ci=None)
plt.show()

msleep['log_bodywt'].corr(msleep['awake'])

# Other transformation
# # Log transformation (log(x))
# # Square root transformation (sqrt(x))
# # Reciprocal transformation (1/x)
# # Combinations of these, e.g.:
# # # log(x) and log(y)
# # # sqrt(x) and 1/y

# Why use a trasformation?
# # Certain statistical methods rely on variables having a linear relationship
# # # Correlation coefficient
# # # Linear regression

# Correlation does not imply causation
# # X is correlated with Y DOES NOT MEAN X cause Y
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

world_happiness = pd.read_csv("./data/world_happiness.csv")

# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)

# Show plot
plt.show()
  
# Correlation between gdp_per_cap and life_exp
cor = world_happiness["gdp_per_cap"].corr(world_happiness["life_exp"])

print(cor)

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of log_gdp_per_cap and happiness_score
sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)