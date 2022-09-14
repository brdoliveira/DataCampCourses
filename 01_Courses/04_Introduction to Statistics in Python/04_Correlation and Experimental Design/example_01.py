"""
# Correlation
# # x = explanatory / independent variable
# # y = response / dependent variable

# Correlation Coefficient
# # Quantifies the linear relationship between two variables
# # Number between -1 and 1
# # Magnitude corresponds to strength of relationship
# # Sign (+ or -) corresponds to direction of relationship
# # # 0.99 (very strong relationship)
# # # 0.75 (strong relationship)
# # # 0.56 (moderate relationship)
# # # 0.21 (weak relationship)
# # # 0.04 (no relationship) -> Knowing the value of X doesn't tell us anything about Y
# # Sign = direction
# # # 0.75: as X increases, Y increases
# # # -0.75: as X increases, Y decreases

import seaborn as sns

sns.scatterplot(x="sleep_total",y="sleep_rem",data=msleep) # no trendline
sns.lmplot(x="sleep_total",y="sleep_rem",data=msleep, ci=None) # with trendline
plt.show()

# Computing correlation
msleep['sleep_total'].corr(msleep['sleep_rem'])
msleep['sleep_rem'].corr(msleep['sleep_total'])
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

world_happiness = pd.read_csv("./data/world_happiness.csv")

# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)

# Show plot
plt.show()

# Correlation between life_exp and happiness_score
cor = world_happiness["life_exp"].corr(world_happiness["happiness_score"])

print(cor)