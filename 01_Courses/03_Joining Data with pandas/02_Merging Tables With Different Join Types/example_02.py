# Other Joins
import pandas as pd

movies = pd.read_pickle('./data/movies.p')

movie_to_genres = pd.read_pickle('./data/movie_to_genres.p')
m = movie_to_genres['genre'] == 'TV Movie'
tv_genre = movie_to_genres[m]
print(tv_genre)

# Right join
tv_movies = movies.merge(tv_genre, how='right',
                        left_on='id',right_on='movie_id')
print(tv_movies.head())

# Outer Join
m = movie_to_genres['genre'] == 'Family'
family = movie_to_genres[m].head(3)

m = movie_to_genres['genre'] == 'Comedy'
comedy = movie_to_genres[m].head(3)

family_comedy = family.merge(comedy, on='movie_id',how='outer',
                            suffixes=('_fam','_com'))