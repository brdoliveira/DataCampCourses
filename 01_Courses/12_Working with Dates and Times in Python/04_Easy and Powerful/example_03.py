from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt

# Import W20529's rides in Q4 2017
rides = pd.read_csv('./data/capital-onebike.csv',
                    parse_dates=['Start date','End date'])

print(rides['Duration'].dt.total_seconds().min())

rides['Start date'].head(3)\
    .dt.tz_localize('America/New_York')

# Try to set a timezone...
# rides['Start date'] = rides['Start date']\
#     .dt.tz_localize('America/New_York')

# Handle ambiguous datetimes
rides['Start date'] = rides['Start date']\
    .dt.tz_localize('America/New_York', ambiguous='NaT')

rides['End date'] = rides['End date']\
    .dt.tz_localize('America/New_York', ambiguous='NaT')

# Re-calculate duation, ignoring bad row
rides['Duration'] = rides['End date'] - rides['Start date']

# Find the minimum again
rides['Duration'].dt.total_seconds().min()

# Look at problematic row
rides.iloc[129]

# Year of first three rows
print(rides['Start date']\
    .head(3)\
    .dt.year)

# See weekday for first three rides
print(
    rides['Start date']\
        .head(3)\
        .dt.day_name()
)

# Shift the indexes forward one, padding with NaT
rides['End date'].shift(1).head(3)