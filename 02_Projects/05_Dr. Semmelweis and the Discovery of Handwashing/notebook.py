import matplotlib.pyplot as plt
import pandas as pd

yearly = pd.read_csv("datasets/yearly_deaths_by_clinic.csv")
print(yearly.head())

yearly["proportion_deaths"] = yearly["deaths"] / yearly["births"]
clinic_1 = yearly[yearly["clinic"] == "clinic 1"]
clinic_2 = yearly[yearly["clinic"] == "clinic 2"]

ax = clinic_1.plot(x="year",y="proportion_deaths", label='Clinic 1',color="g")
clinic_2.plot(x="year",y="proportion_deaths", label='Clinic 2',color="r",ax=ax)
plt.show()

monthly = pd.read_csv("datasets/monthly_deaths.csv",parse_dates=["date"])
monthly["proportion_deaths"] = monthly["deaths"] / monthly["births"]
print(monthly.head())

ax = monthly.plot(x="date",y="proportion_deaths",ylabel="Proportion deaths")

handwashing_start = pd.to_datetime('1847-06-01')
before_washing = monthly[monthly["date"] < handwashing_start]
after_washing = monthly[monthly["date"] >= handwashing_start]

ax = before_washing.plot(x="date",
                         y="proportion_deaths",
                         label="Before Washing",
                         color="gray")

after_washing.plot(x="date",
                   y="proportion_deaths",
                   label="After Washing",
                   color="red",
                   ax=ax)

ax.axvline(x='1847-06-01', color='black')
plt.show()

before_proportion = before_washing['proportion_deaths']
after_proportion = after_washing['proportion_deaths']
mean_diff = after_proportion.mean() - before_proportion.mean()
print(mean_diff)

boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac = 1, replace = True)
    boot_after = after_proportion.sample(frac = 1, replace = True)
    boot_mean_diff.append(boot_after.mean() - boot_before.mean())

confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
print(confidence_interval)

doctors_should_wash_their_hands = True