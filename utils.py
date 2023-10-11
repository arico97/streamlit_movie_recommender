import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('./movies_metadata.csv',low_memory='False')
# df= df_r.iloc[:5000,:]
# Define a TF-IDF Vectorizer Object. Remove all english stopwords
tfidf = TfidfVectorizer(stop_words='english')
#tfidf = TfidfVectorizer(stop_words='english',max_df = 0.9, min_df=0.1,max_features = 500)
# Replace NaN with an empty string
df['overview'] = df['overview'].fillna('')
# Construct the required TF-IDF matrix by applying the fit_transform method on the overview feature

# tfidf_matrix = tfidf.fit_transform(df['overview'])
tfidf_matrix = tfidf.fit_transform(df['overview'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


del tfidf_matrix
indices = pd.Series(df.index, index=df['title']).drop_duplicates()


def content_recommender(title,cosine_sim=cosine_sim ,df = df,indices = indices):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]