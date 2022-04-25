import pandas as pd
import datetime as dt

from psutil import users

flights = pd.read_csv('./data/flights.csv')
flights.head()

sum_classes = flights[['economy_class','business_class','first_class']].sum(axis=1)
passenger_equ = sum_classes == flights['total_passengers']

# Find and filter out rows with inconsistent passenger totals
inconsistent_pass = flights[~passenger_equ]
consistent_pass = flights[passenger_equ]


users = pd.read_csv("./data/users.csv")
# Convert to datetime and get today´s date
users['Birthday'] = pd.to_datetime(users['Birthday'])
today = dt.date.today()

# For each row in the Birthday column, calculate year difference
age_manual = today.year - users['Birthday'].dt.year

# Find instances where ages match
age_equ = age_manual == users['Age']

# Find and filter out rows with inconsistent age
inconsistent_age = users[~age_equ]
consistent_age = users[age_equ]