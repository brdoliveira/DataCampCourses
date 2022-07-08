"""
# Centering and scaling
"""
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np

music_df = pd.read_csv('./data/music_clean.csv')
# print(music_df.info())

# Why scale our data?
print(music_df[["duration_ms","loudness","speechiness"]].describe())

# Why scale our data?
# # Many models use some form of distance to inform them
# # Features on larger scales can disproportionately influence the model
# # Example: KNN uses distance explicitly when making predictions
# # We want features to be on a similar scale
# # Normalizing or standardizing (scaling and centering)

# How to scale our data
# # Subtract the mean and divide by variance
# # # All features are centered around zero and have a variance of one
# # # This is called standardization
# # Can also subtract the minimum and divide by the range
# # # Minimum zero and maximum one
# # Can also normalize so the data ranges from -1 to +1
# # See scikit-learn docs for further details

X = music_df.drop("genre", axis=1).values
y = music_df["genre"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(np.mean(X), np.std(X))
print(np.mean(X_train_scaled), np.std(X_train_scaled))


# Scaling in a pipeline
steps = [('scaler', StandardScaler()),('knn', KNeighborsClassifier(n_neighbors=6))]
pipeline = Pipeline(steps)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=21)

knn_scaled = pipeline.fit(X_train, y_train)
y_pred = knn_scaled.predict(X_test)

print(knn_scaled.score(X_test, y_test))

# Comparing performance using unscaled data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=21)
knn_unscaled = KNeighborsClassifier(n_neighbors=6).fit(X_train, y_train)
print(knn_unscaled.score(X_test, y_test))

# CV and scaling in a pipeline
steps = [('scaler', StandardScaler()),('knn', KNeighborsClassifier())]
pipeline = Pipeline(steps)
parameters = {"knn__n_neighbors": np.arange(1, 50)}

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=21)
cv = GridSearchCV(pipeline, param_grid=parameters)
cv.fit(X_train, y_train)

y_pred = cv.predict(X_test)

# Checking model parameters
print(cv.best_score_)
print(cv.best_params_)