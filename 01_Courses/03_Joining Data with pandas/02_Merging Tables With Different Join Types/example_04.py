# Merging on indexes
import pandas as pd

movies = pd.read_pickle('./data/movies.p')
# movies = pd.read_csv('movies.csv',index=['id])
print(movies.head())
print('*' * 30)

taglines = pd.read_pickle('./data/taglines.p')
print(taglines.head())
print('*' * 30)

movies_taglines = movies.merge(taglines, on='id', how='left')
print(movies_taglines.head())
print('*' * 30)

# # MultiIndex datasets
# samuel = pd.read_csv('samuel.csv', index_col=['movie_id','cast_id'])
# casts = pd.read_csv('casts.csv', index_col=['movie_id','cast_id'])
# samuel_casts = samuel.merge(casts,on=['movie_id','cast_id'])

# # Index merge with left_on and right_on
# movies_genres = movies.merge(movie_to_genres,left_on='id',left_index=True,
#                             righr_on='movie_id',right_index=True)
# print(movies_genres.head())