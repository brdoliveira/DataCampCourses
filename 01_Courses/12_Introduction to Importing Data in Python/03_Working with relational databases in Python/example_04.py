'''
from sqlalchemy import create_engine
import pandas as pd

file_path = './data/Chinook.sqlite'
engine = create_engine('sqlite:///' + file_path)
df = pd.read_sql_query("SELECT OrderID, CompanyName FROM Orders INNER JOIN  Custumers on Orders.CustumerID = Custumers.CustumerID",engine)
print(df.head())
'''
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
file_path = './data/Chinook.sqlite'
engine = create_engine("sqlite:///" + file_path)

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())

print("*" * 60)
# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000",engine)

# Print head of DataFramea
print(df.head())