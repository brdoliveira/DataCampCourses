import pandas as pd
import matplotlib.pyplot as plt

temperatures = pd.read_csv("./data/temperatures.csv")
temperatures.head()

plt.scatter(x='Date',y='Temperature',data=temperatures)
# Create title, xlabel and ylabel
plt.title('Temperature in Celsius March 2019 - NYC')
plt.xlabel('Dates')
plt.ylabel('Temperature in Celsius')
# Show plot
plt.show()

temp_fah = temperatures.loc[temperatures['Temperatures'] > 40,'Temperatures']
temp_cels = (temp_fah - 32) * (5/9)
temperatures.loc[temperatures['Temperatures'] > 40,'Temperatures'] = temp_cels

# Asssert conversion is correct
assert temperatures['Temperatures'].max() < 40


birthdays = pd.read_csv("./data/birthday.csv")
# Converts to datetime
birthdays['Birthday'] = pd.to_datetime(birthdays['Birthday'],
                                        # Attempt to infer format of each date
                                        infer_datetime_format=True,
                                        # Return NA for rows where conversion failed
                                        errors='coerce')

birthdays['Birthday'] = birthdays['Birthday'].dt.strftime("%d-%m-%Y")
birthdays.head()