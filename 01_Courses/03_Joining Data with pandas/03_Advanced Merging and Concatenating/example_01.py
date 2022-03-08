# Filtering Joins

# Semi join
genres_tracks = genres.merge(top_tracks, on='gid')
print(genre_tracks.head())

top_genres = genres[genres['gid'].isin(genres_tracks['gid'])]
print(top_genres.head())


# Anti join 
genres_tracks = genres.merge(top_tracks,on='gid',how='left',indicador=True) # indicador -> add column name 

grid_list = genres_tracks.loc[genres_track['_merge'] == 'left_only','gid']
print(grid_list.head())

non_top_genres = genres[genres['gid'].isin(gid_list)]
print(non_top_genres.head())
