'''
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqllite://Northwind.sqlite')
con = engine.connect()
rs = con.execute("SELECT * FROM ORDERS")

df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()
con.close()


print(df.head())

with engine.connect() as con:
    rs = con.execute("SELECT OrderID, OrderDate, ShipName from Orders")
    df = pd.DataFrame(rs.fetchmany(size=5)) # 5 rows
    df.columns = rs.keys()
'''

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
file_path = './data/Chinook.sqlite'
engine = create_engine('sqlite:///' + file_path)

# Open engine connection: con
con = engine.connect()

# Perform query: rs
print("Select * from Album")
rs = con.execute("Select * from Album")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()


# Close connection
con.close()


# Print head of DataFrame df
print(df.head())

print("*" * 60)
print("SELECT LastName,Title from Employee")
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT LastName,Title from Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())

# Print the length of the DataFrame df
print(f'Len Df ={len(df)}')

print("*" * 60)
print("Select * from Employee where EmployeeId >= 6")
# Create engine: engine
engine = create_engine('sqlite:///' + file_path)

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("Select * from Employee where EmployeeId >= 6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())

print("*" * 60)

# Create engine: engine
engine = create_engine('sqlite:///' + file_path)

# Open engine in context manager
print("SELECT * FROM Employee ORDER BY BirthDate")
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee ORDER BY BirthDate")
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())
