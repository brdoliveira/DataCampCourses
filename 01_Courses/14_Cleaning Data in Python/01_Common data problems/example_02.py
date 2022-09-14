'''
import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv("./data/movies.csv")
movies.head()

plt.hist(movies['avg_rating'])
plt.title('Average rating of movies (1-5)')
plt.show()

# Import date type
import data as dt

user_signups = pd.read_csv("./data/user_signups.csv")

today_date = dt.date.today()
user_signups[user_signups['subscription_date'] > dt.date.today()]

# Output data types
user_signups.dtypes

# Convert to date
user_signups['subscription_date'] = pd.to_datetime(user_signups['subscription_date']).dt.date

# DROP DATA
# Drop values  values using filtering
user_signups = user_signups[user_signups['subscription_date'] < today_date]
# Drop values using .drop
user_signups.drop(user_signups[user_signups['subscription_date'] > today_date].index,inplace= True)

## HARDCORE DATES WITH UPPER LIMIT
# Drop values using filtering
user_signups.loc[user_signups['subscription_date'] > today_date, 'subscription_date'] = today_date
# Assert is true
assert user_signups['subscription_date'].max().date() <= today_date

# Output Movies with rating > 5
movies[movies['avg_rating'] > 5]

# Drop values using filtering
movies = movies[movies['avg_rating'] <= 5]
# Drop values using .drop()
movies.drop(movies[movies['avg_rating'] > 5].index,inplace= True)

# Assert results
assert movies['avg_rating'].max() <= 5

# Convert avg_rating > 5 to 5
movies.loc[movies['avg_rating'] > 5,'avg_rating'] = 5

# Asssert statement
assert movies['avg_rating'].max() <= 5
# Remember, no output means it passed
'''