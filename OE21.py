import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the movies.csv and user.csv files into dataframes
movies_df = pd.read_csv("merged_file.csv")
user_df = pd.read_csv("Usuario_0.csv", delimiter=';')

# Merge the two dataframes on the "movieId" column
merged_df = pd.merge(movies_df, user_df, on="movieId")

# Define the feature matrix
X = merged_df["plot_summary"] + merged_df["genres"].apply(lambda x: ' '.join(x))

# Vectorize the feature matrix
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(X)

# Use the "rating" column as the target
y = merged_df["rating"]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict the rating for a specific movie using its movieId
input_movie = movies_df[movies_df["movieId"] == 3]
input_features = tfidf.transform(input_movie["plot_summary"] + ' ' + input_movie["genres"].apply(lambda x: ' '.join(x)))
predicted_rating = model.predict(input_features)

print(predicted_rating)


