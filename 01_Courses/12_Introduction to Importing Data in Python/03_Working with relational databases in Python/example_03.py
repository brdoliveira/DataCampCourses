'''
from sqlalchemy import create_engine
import pandas as pd

file_path = './data/Chinook.sqlite'
engine = create_engine("sqllite:///" + file_path)
df = pd.read_sql_query("SELECT * FROM Album",engine)
'''

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
file_path = './data/Chinook.sqlite'
engine = create_engine("sqlite:///" + file_path)

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * from Album", engine)

# Print head of DataFrame
print(df.head())
print("*" * 60)

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))


print("*" * 60)

# Create engine: engine
engine = create_engine("sqlite:///" + file_path)

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate", engine)

# Print head of DataFrame
print(df.head())