"""
# Preprocessing data

# scikit-learn requirements
# # Numeric data
# # No missing values
# With real-world data:
# # This is rarely the case
# # We will often need to preprocess our data rst

# Dealing with categorical features
# # scikit-learn will not accept categorical features by default
# # Need to convert categorical features into numeric values
# # Convert to binary features called dummy variables
# # # 0: Observation was NOT that category
# # # 1: Observation was that category

# Dealing with categorical features in Python
# # scikit-learn: OneHotEncoder()
# # pandas: get_dummies()
"""
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

music_df = pd.read_csv('./data/music_clean.csv')
print(music_df.info())

# Encoding dummy variables
music_dummies = pd.get_dummies(music_df["genre"], drop_first=True)
print(music_dummies.head())

music_dummies = pd.concat([music_df, music_dummies], axis=1)
music_dummies = music_dummies.drop("genre", axis=1)

music_dummies = pd.get_dummies(music_df, drop_first=True)
print(music_dummies.columns)

# Linear regression with dummy variables

X = music_dummies.drop("popularity", axis=1).values
y = music_dummies["popularity"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)
kf = KFold(n_splits=5, shuffle=True, random_state=42)
linreg = LinearRegression()
linreg_cv = cross_val_score(linreg, X_train, y_train, cv=kf,scoring="neg_mean_squared_error")
print(np.sqrt(-linreg_cv))