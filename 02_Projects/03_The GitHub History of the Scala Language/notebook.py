import pandas as pd
import matplotlib.pyplot as plt

pulls_one = pd.read_csv('datasets/pulls_2011-2013.csv')
pulls_two = pd.read_csv('datasets/pulls_2014-2018.csv')
pull_files = pd.read_csv('datasets/pull_files.csv') 

pulls = pulls_one.append(pulls_two)

pulls['date'] = pd.to_datetime(pulls['date'],utc=True)

data = pulls.merge(pull_files,on="pid")

data['month'] = data["date"].dt.month

data['year'] = data["date"].dt.year

counts = data.groupby(["month", "year"]).agg({"pid":"count"})

ax = counts.plot(kind='bar', figsize = (18,6))

by_user = data.groupby("user", as_index = False).agg({"pid":"count"})

ax = by_user.plot(kind="hist")

last_10 = pulls.nlargest(10,columns ="date")

joined_pr = last_10.merge(pull_files,on="pid")

files = set(joined_pr["file"])
print(files.head())

file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

file_pr = data[data["file"] == file]

author_counts = file_pr.groupby("user").agg({"pid":"count"})

author_counts.nlargest(3,columns="pid")

file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

file_pr = pull_files[pull_files["file"] == file]

joined_pr = file_pr.merge(pulls,on="pid")

users_last_10 = set(joined_pr.nlargest(10,columns="date")["user"])
print(users_last_10.head())

authors = ['xeno-by', 'soc']

by_author = pulls[pulls["user"].isin(authors)]

counts = by_author.groupby(["user",by_author["date"].dt.year]).agg({'pid': 'count'}).reset_index()

counts_wide = counts.pivot_table(index='date', columns='user', values='pid', fill_value=0)

ax = counts_wide.plot(kind="bar")

authors = ['xeno-by', 'soc']
file = 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

by_author = data[data["user"].isin(authors)]

by_file = by_author[by_author["file"] == file]

grouped = by_file.groupby(['user', by_file['date'].dt.year]).count()['pid'].reset_index()

by_file_wide = grouped.pivot_table(index='date',columns='user',values='pid',fill_value=0)

by_file_wide.plot(kind='bar')

plt.show()