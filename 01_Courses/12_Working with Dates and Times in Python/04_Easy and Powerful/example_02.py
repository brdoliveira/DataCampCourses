from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt

# Import W20529's rides in Q4 2017
rides = pd.read_csv('./data/capital-onebike.csv',
                    parse_dates=['Start date','End date'])

rides['Duration'] = rides['End date'] - rides['Start date']

# Avarage time out of the dock
print("Mean:")
print(rides['Duration'].mean()) # You can call mean() , median() and sum()

print("Sum:")
print(rides['Duration'].sum())

# Percent of time out of the dock
print("Percent of time out of the dock:")
print(rides['Duration'].sum() / timedelta(days=91))

# Count how many time the bike started at each station
print(rides["Member type"].value_counts())

# Percent of rides by member
print(rides['Member type'].value_counts() / len(rides))

# Add duration (in seconds) column
rides['Duration seconds'] = rides['Duration'].dt.total_seconds()

# Average duration per member type
print(rides.groupby('Member type')['Duration seconds'].mean())

# Average duration by month
print(rides.resample('M',on='Start date')['Duration seconds'].mean())

# Size per group 
rides.groupby('Member type').size()

# First ride per group
rides.groupby('Member type').first()

rides\
    .resample('M', on='Start date')\
    ['Duration seconds']\
    .mean()\
    .plot()

rides\
    .resample('D', on='Start date')\
    ['Duration seconds']\
    .mean()\
    .plot()

plt.show()