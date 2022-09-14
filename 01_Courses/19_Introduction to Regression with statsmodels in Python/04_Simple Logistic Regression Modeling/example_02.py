"""
# Predictions and odds rations
# # The regplot() predictions
sns.regplot(x="time_since_last_purchase",
            y="has_churned",
            data=churn,
            ci=None,
            logistic=True)

plt.show()

# Making predictions
mdl_recency = logit("has_churned ~ time_since_last_purchase", data=churn).fit()

explanatory_data = pd.DataFrame(
    {"time_since_last_purchase": np.arange(-1,6.25,0.25)}
)

prediction_data = explanatory_data.assign(
    has_churned = mdl_recency.predict(explanatory_data)
)

# Adding point predictions

sns.regplot(x="time_since_last_purchase",
            y="has_churned",
            data=churn,
            ci=None,
            logistic=True)

sns.scatterplot(x="time_since_last_purchase",
                y="has_churned",
                data=prediction_data,
                color="red")

plt.show()

# Getting the most likely outcome
prediction_data = explanatory_data.assign(
    has_churned = mdl_recency.predict(explanatory_data))
prediction_data["most_likely_outcome"] = np.round(prediction_data["has_churned"])

# Visualizing most likely outcome

sns.regplot(x="time_since_last_purchase",
            y="has_churned",
            data=churn,
            ci=None,
            logistic=True)

sns.scatterplot(x="time_since_last_purchase",
                y="most_likely_outcome",
                data=prediction_data,
                color="red")

plt.show()

# Odds ratios
# # Odds ratios is the probability of something happening divided by the probability that it doesn't
odds_ratio = probability / (1 - probability)

# Calculating odds ratio
prediction_data["odds_ratio"] = prediction_data["has_churned"] / ( 1 - prediction_data["has_churned"] )

# Visualing odds ratio
sns.lineplot(x="time_since_last_purchase",
             y="odds_ratio",
             data=prediction_data)

plt.axhline(y=1, linestyle="dotted")
plt.yscale("log")

plt.show()

# Calculating log odds ratios
prediction_data["log_odds_ratio"] = np.log(prediction_data["odds_ratio"])


"""