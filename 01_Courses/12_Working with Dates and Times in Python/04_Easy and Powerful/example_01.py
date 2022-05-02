import pandas as pd

# Import W20529's rides in Q4 2017
rides = pd.read_csv('./data/capital-onebike.csv')
print(rides.head(3))

print(rides['Start date'])
print(rides.iloc[2])

rides = pd.read_csv('./data/capital-onebike.csv',
                    parse_dates=['Start date','End date'])

# Or:
rides['Start date'] = pd.to_datetime(rides['Start date'],
                                    format="%Y-%m-%d %H:%M:%S")

# Select Start date for row 2
rides['Start date'].iloc[2]

# Create a duration column 
rides['Duration'] = rides['End date'] - rides['Start date']

# print(rides['Duration'].head())
print(rides['Duration']\
    .dt.total_seconds()\
    .head())