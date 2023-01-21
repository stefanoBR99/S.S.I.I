import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer


# read the first csv file into a dataframe
df1 = pd.read_csv("moviestest.csv")
# read the second csv file into a dataframe
df2 = pd.read_csv("linkstest_new.csv")

# merge the two dataframes on the 'id' column
merged_df = pd.merge(df1, df2, on='movieId')


#Import TfIdfVectorizer from scikit-learn
#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
from nltk.corpus import stopwords

spanish_stopwords = stopwords.words('spanish')

tfidf = TfidfVectorizer(stop_words= spanish_stopwords)

#Replace NaN with an empty string

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(merged_df['plot_summary'])

#Output the shape of tfidf_matrix
print(tfidf_matrix.shape)

# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(merged_df.index, index=merged_df['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return merged_df['title'].iloc[movie_indices]


print(get_recommendations('Jumanji (1995)'))