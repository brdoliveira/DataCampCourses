'''
from sqlalchemy import create_engine
import pandas as pd

file_path = './data/Chinook.sqlite'
engine = create_engine('sqlite:///' + file_path)
df = pd.read_sql_query("SELECT OrderID, CompanyName FROM Orders INNER JOIN  Custumers on Orders.CustumerID = Custumers.CustumerID",engine)
print(df.head())
'''