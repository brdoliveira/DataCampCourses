"""
# Why you need logistic regression

|# Churn vs. recency: a linear model
mdl_churn_vs_recency = ols("has_churned ~ time_since_last_purchase",data=churn).fit()
print(mdl_churn_vs_recency_lm.params)

intercept, slope = mdl_churn_vs_recency_lm.params

# Visualizing the linear model
sns.scatterplot(x="time_since_last_purchase",
                y="has_churned",
                data=churn)

plt.axline(xy1=(0,intercept),slope=slope)

plt.xlim(-10,10)
plt.ylim(-0.2,1.2)

plt.show()

# What is a logistic regression?
# # Another type of generalized linear mode.
# # Used when the response variable is logical.
# # The response follow logistic (S-sharped) curve.
from statsmodels.formula.api import logit

mdl_churn_vs_recency_logit = logit("has_churned ~ time_since_last_purchase", data=churn).fit()
print(mdl_churn_vs_recency_logit.params)

# Visualing the logistic model
sns.regplot(x="time_since_last_purchase",
            y="has_churned",
            data=churn,
            ci=None,
            logistic=True)

plt.axline(xy1=(0,intercept),
           slope=slope,
           color="black")

plt.show()

# + buy high closer to 1
# - low purchase closer to 0

"""