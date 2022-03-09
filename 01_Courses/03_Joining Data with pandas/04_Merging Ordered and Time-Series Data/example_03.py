# .query() -> "SQL"
import pandas as pd

stocks = pd.read_csv('./data/stocks.csv')

stocks.query('nike >=90')
stocks.query('nike > 90 and disney < 140')
stocks.query('nike > 96 or disney < 98')

stocks_long = pd.read_csv('./data/stocks_long.csv')
stocks_long.quey('stock=="disney" or (stock="nike" and close < 90)')
