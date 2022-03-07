# Left Join
import pandas as pd

movies = pd.read_pickle('./data/movies.p')
print(movies.head())
print(movies.shape)
print('*' * 30) 

taglines = pd.read_pickle('./data/taglines.p')
print(taglines.head())
print(movies.shape)
print('*' * 30) 


movies_taglines = movies.merge(taglines, on='id', how='left')
print(movies_taglines.head())
print('*' * 30) 
