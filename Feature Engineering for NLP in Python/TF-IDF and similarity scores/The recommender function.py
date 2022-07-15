# In this exercise, we will build a recommender function get_recommendations(), as discussed in the lesson and the previous exercise. As we know, it takes in a title, a cosine similarity matrix, and a movie title and index mapping as arguments and outputs a list of 10 titles most similar to the original title (excluding the title itself).

# You have been given a dataset metadata that consists of the movie titles and overviews. The head of this dataset has been printed to console.

# Instructions
# Get index of the movie that matches the title by using the title key of indices.
# Extract the ten most similar movies from sim_scores and store it back in sim_scores.

# Generate mapping between titles and index
indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

def get_recommendations(title, cosine_sim, indices):
    # Get index of movie that matches title
    idx = indices[title]
    # Sort the movies based on the similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores for 10 most similar movies
    sim_scores = sim_scores[1:11]
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    # Return the top 10 most similar movies
    return metadata['title'].iloc[movie_indices]
  
#  TED talk recommender

# In this exercise, we will build a recommendation system that suggests TED Talks based on their transcripts. You have been given a get_recommendations() function that takes in the title of a talk, a similarity matrix and an indices series as its arguments, and outputs a list of most similar talks. indices has already been provided to you.

# You have also been given a transcripts series that contains the transcripts of around 500 TED talks. Your task is to generate a cosine similarity matrix for the tf-idf vectors of the talk transcripts.

# Consequently, we will generate recommendations for a talk titled '5 ways to kill your dreams' by Brazilian entrepreneur Bel Pesce.

# Instructions
# Initialize a TfidfVectorizer with English stopwords. Name it tfidf.
# Construct tfidf_matrix by fitting and transforming transcripts.
# Generate the cosine similarity matrix cosine_sim using tfidf_matrix.
# Use get_recommendations() to generate recommendations for '5 ways to kill your dreams'.

# Initialize the TfidfVectorizer 
tfidf = TfidfVectorizer(stop_words='english')

# Construct the TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(transcripts)

# Generate the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix,tfidf_matrix)
 
# Generate recommendations 
print(get_recommendations('5 ways to kill your dreams', cosine_sim, indices))

# 453             Success is a continuous journey
# 157                        Why we do what we do
# 494                   How to find work you love
# 149          My journey into movies that matter
# 447                        One Laptop per Child
# 230             How to get your ideas to spread
# 497         Plug into your hard-wired happiness
# 495    Why you will fail to have a great career
# 179             Be suspicious of simple stories
# 53                          To upgrade is human
# Name: title, dtype: object
