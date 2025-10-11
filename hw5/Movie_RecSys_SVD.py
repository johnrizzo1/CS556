# Movie_RecSys_SVD
# %% [markdown]
# # Movie Recommendations HW

# %% [markdown]
# **Name:**  

# %% [markdown]
# **Collaboration Policy:** Homeworks will be done individually: each student must hand in their own answers. Use of partial or entire solutions obtained from others or online is strictly prohibited.

# %% [markdown]
# **Late Policy:** Late submission have a penalty of 2\% for each passing hour. 

# %% [markdown]
# **Submission format:** Successfully complete the Movie Lens recommender as described in this jupyter notebook. Submit a `.py` and an `.ipynb` file for this notebook. You can go to `File -> Download as ->` to download a .py version of the notebook. 
# 
# **Only submit one `.ipynb` file and one `.py` file.** The `.ipynb` file should have answers to all the questions. Do *not* zip any files for submission. 

# %% [markdown]
# **Download the dataset from here:** https://grouplens.org/datasets/movielens/1m/

# %%
# Import all the required libraries
import numpy as np
import pandas as pd

# %% [markdown]
# ## Reading the Data
# Now that we have downloaded the files from the link above and placed them in the same directory as this Jupyter Notebook, we can load each of the tables of data as a CSV into Pandas. Execute the following provided code.

# %%
# Read the dataset from the two files into ratings_data and movies_data
# NOTE: if you are getting a decode error, add "encoding='ISO-8859-1'" as an additional argument
#       to the read_csv function
column_list_ratings = ["UserID", "MovieID", "Ratings","Timestamp"]
ratings_data  = pd.read_csv('ratings.dat',sep='::',names = column_list_ratings, engine='python')
column_list_movies = ["MovieID","Title","Genres"]
movies_data = pd.read_csv('movies.dat',sep = '::',names = column_list_movies, engine='python', encoding = 'latin-1')
column_list_users = ["UserID","Gender","Age","Occupation","Zixp-code"]
user_data = pd.read_csv("users.dat",sep = "::",names = column_list_users, engine='python')

# %% [markdown]
# `ratings_data`, `movies_data`, `user_data` corresponds to the data loaded from `ratings.dat`, `movies.dat`, and `users.dat` in Pandas.

# %% [markdown]
# ## Data Analysis

# %% [markdown]
# We now have all our data in Pandas - however, it's as three separate datasets! To make some more sense out of the data we have, we can use the Pandas `merge` function to combine our component data-frames. Run the following code:

# %%
data = pd.merge(pd.merge(ratings_data,user_data),movies_data)
data

# %% [markdown]
# Next, we can create a pivot table to match the ratings with a given movie title. Using `data.pivot_table`, we can aggregate (using the average/`mean` function) the reviews and find the average rating for each movie. We can save this pivot table into the `mean_ratings` variable. 

# %%
mean_ratings = data.pivot_table('Ratings','Title',aggfunc = 'mean')
mean_ratings

# %% [markdown]
# Now, we can take the `mean_ratings` and sort it by the value of the rating itself. Using this and the `head` function, we can display the top 15 movies by average rating.

# %%
mean_ratings = data.pivot_table('Ratings',index = ["Title"],aggfunc = 'mean')
top_15_mean_ratings = mean_ratings.sort_values(by = 'Ratings',ascending = False).head(15)
top_15_mean_ratings

# %% [markdown]
# Let's adjust our original `mean_ratings` function to account for the differences in gender between reviews. This will be similar to the same code as before, except now we will provide an additional `columns` parameter which will separate the average ratings for men and women, respectively.

# %%
mean_ratings = data.pivot_table('Ratings',index = ["Title"],columns = ["Gender"],aggfunc = 'mean')
mean_ratings

# %% [markdown]
# We can now sort the ratings as before, but instead of by `Rating`, but by the `F` and `M` gendered rating columns. Print the top rated movies by male and female reviews, respectively.

# %%
data = pd.merge(pd.merge(ratings_data,user_data),movies_data)

mean_ratings = data.pivot_table('Ratings',index = ["Title"],columns = ["Gender"],aggfunc = 'mean')
top_female_ratings = mean_ratings.sort_values(by = 'F', ascending = False)
print(top_female_ratings.head(15))

top_male_ratings = mean_ratings.sort_values(by = 'M', ascending = False)
print(top_male_ratings.head(15))

# %%
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by = 'diff')
sorted_by_diff[:10]

# %% [markdown]
# Let's try grouping the data-frame, instead, to see how different titles compare in terms of the number of ratings. Group by `Title` and then take the top 10 items by number of reviews. We can see here the most popularly-reviewed titles.

# %%
ratings_by_title = data.groupby('Title').size()
ratings_by_title.sort_values(ascending = False).head(10)

# %% [markdown]
# Similarly, we can filter our grouped data-frame to get all titles with a certain number of reviews. Filter the dataset to get all movie titles such that the number of reviews is >= 2500.

# %% [markdown]
# ## Question 1

# %% [markdown]
# Create a ratings matrix using Numpy. This matrix allows us to see the ratings for a given movie and user ID. The element at location $[i,j]$ is a rating given by user $i$ for movie $j$. Print the **shape** of the matrix produced.  
# 
# Additionally, choose 3 users that have rated the movie with MovieID "**1377**" (Batman Returns). Print these ratings, they will be used later for comparison.
# 
# 
# **Notes: (READ CAREFULLY)**
# - Do *not* use `pivot_table`.
# - A ratings matrix is *not* the same as `ratings_data` from above.
# - The ratings of movie with MovieID $i$ are stored in the ($i$-1)th column (index starts from 0)  
# - Not every user has rated every movie. Missing entries should be set to 0 for now.
# - If you're stuck, you might want to look into `np.zeros` and how to use it to create a matrix of the desired shape.
# - Every review lies between 1 and 5.

# %%
ratings_data.UserID.max()

# %%
# Create the ratings matrix using Numpy
# Get the maximum user ID and movie ID to determine matrix dimensions
n_users = ratings_data['UserID'].max()
n_movies = ratings_data['MovieID'].max()

# Initialize a matrix of zeros with shape (n_users, n_movies)
ratings_matrix = np.zeros((n_users, n_movies))

# Populate the matrix with ratings
# For each rating, place it at position [user_id-1, movie_id-1] (0-indexed)
for row in ratings_data.itertuples():
    user_id = row.UserID - 1  # Convert to 0-indexed
    movie_id = row.MovieID - 1  # Convert to 0-indexed
    rating = row.Ratings
    ratings_matrix[user_id, movie_id] = rating

# Print the shape of the matrix
print(f"Shape of ratings matrix: {ratings_matrix.shape}")

# %%
# Find 3 users who have rated movie with MovieID 1377 (Batman Returns)
# MovieID 1377 is at column index 1376 (0-indexed)
movie_id_1377 = 1377
column_index = movie_id_1377 - 1  # 0-indexed column

# Get all users who rated this movie (non-zero ratings)
users_who_rated = np.where(ratings_matrix[:, column_index] > 0)[0]

# Select first 3 users who rated this movie
selected_users = users_who_rated[:3]

print(f"\nThree users who rated movie with MovieID {movie_id_1377} (Batman Returns):")
for user_idx in selected_users:
    user_id = user_idx + 1  # Convert back to 1-indexed for display
    rating = ratings_matrix[user_idx, column_index]
    print(f"User {user_id}: Rating = {int(rating)}")

# %% [markdown]
# ## Question 2

# %% [markdown]
# Normalize the ratings matrix (created in **Question 1**) using Z-score normalization. While we can't use `sklearn`'s `StandardScaler` for this step, we can do the statistical calculations ourselves to normalize the data.
# 
# Before you start:
# - Your first step should be to get the average of every *column* of the ratings matrix (we want an average by title, not by user!).
# - Make sure that the mean is calculated considering only non-zero elements. If there is a movie which is rated only by 10 users, we get its mean rating using (sum of the 10 ratings)/10 and **NOT** (sum of 10 ratings)/(total number of users)
# - All of the missing values in the dataset should be replaced with the average rating for the given movie. This is a complex topic, but for our case replacing empty values with the mean will make it so that the absence of a rating doesn't affect the overall average, and it provides an "expected value" which is useful for computing correlations and recommendations in later steps.
# - In our matrix, 0 represents a missing rating.
# - Next, we want to subtract the average from the original ratings thus allowing us to get a mean of 0 in every *column*. It may be very close but not exactly zero because of the limited precision `float`s allow.
# - Lastly, divide this by the standard deviation of the *column*.
# 
# - Not every MovieID is used, leading to zero columns. This will cause a divide by zero error when normalizing the matrix. Simply replace any NaN values in your normalized matrix with 0.

# %%
# Step 1: Calculate the mean of each column (movie), considering only non-zero ratings
# Create a mask for non-zero elements
non_zero_mask = ratings_matrix != 0
non_zero_mask

# %%
# Count non-zero elements per column (movie)
count_non_zero = np.sum(non_zero_mask, axis=0)
count_non_zero

# %%
# Sum of ratings per column
sum_ratings = np.sum(ratings_matrix, axis=0)
sum_ratings

# %%
# Calculate mean for each column (avoiding division by zero)
# If a movie has no ratings, its mean will be 0
column_means = np.divide(sum_ratings, count_non_zero, 
                         out=np.zeros_like(sum_ratings), 
                         where=count_non_zero != 0)
column_means

# %%
print(f"Sample column means (first 10 movies): {column_means[:10]}")
print(f"Number of movies with no ratings: {np.sum(count_non_zero == 0)}")

# %%
# Step 2: Replace missing values (zeros) with the column mean
# Create a copy of the ratings matrix to fill
filled_matrix = ratings_matrix.copy()

# For each column, replace 0s with the column mean
for col in range(filled_matrix.shape[1]):
    mask = filled_matrix[:, col] == 0
    filled_matrix[mask, col] = column_means[col]

print(f"Shape of filled matrix: {filled_matrix.shape}")
print(f"Number of zeros remaining: {np.sum(filled_matrix == 0)}")

# %%
# Step 3: Subtract the mean from each column (centering)
centered_matrix = filled_matrix - column_means

# Verify that column means are approximately 0
new_means = np.mean(centered_matrix, axis=0)
print(f"Sample new column means (should be ~0): {new_means[:10]}")
print(f"Max absolute mean after centering: {np.max(np.abs(new_means))}")

# %%
# Step 4: Calculate standard deviation for each column
column_std = np.std(centered_matrix, axis=0)

print(f"Sample column standard deviations (first 10): {column_std[:10]}")
print(f"Number of columns with zero std: {np.sum(column_std == 0)}")

# %%
# Step 5: Normalize by dividing by standard deviation
# Avoid division by zero by only dividing where std > 0
normalized_matrix = np.divide(centered_matrix, column_std,
                              out=np.zeros_like(centered_matrix),
                              where=column_std != 0)

# Step 6: Replace any NaN values with 0 (from movies with no variance)
normalized_matrix = np.nan_to_num(normalized_matrix, nan=0.0)
normalized_matrix

# %%
print(f"Shape of normalized matrix: {normalized_matrix.shape}")
print(f"Number of NaN values: {np.sum(np.isnan(normalized_matrix))}")
print(f"Sample normalized values (first user, first 10 movies): {normalized_matrix[0, :10]}")

# Verify normalization: check a few columns have mean~0 and std~1
sample_cols = [0, 100, 500, 1000]
for col in sample_cols:
    if column_std[col] > 0:  # Only check columns that had variance
        col_mean = np.mean(normalized_matrix[:, col])
        col_std = np.std(normalized_matrix[:, col])
        print(f"Column {col}: mean={col_mean:.6f}, std={col_std:.6f}")

# %% [markdown]
# ## Question 3

# %% [markdown]
# We're now going to perform Singular Value Decomposition (SVD) on the normalized ratings matrix from the previous question. Perform the process using numpy, and along the way print the shapes of the $U$, $S$, and $V$ matrices you calculated.

# %%
# Compute the SVD of the normalized matrix
# SVD decomposes the matrix A into: A = U * S * V^T
# where:
# - U: left singular vectors (users in our case)
# - S: singular values (diagonal matrix, returned as 1D array)
# - V^T: right singular vectors transposed (movies in our case)

U, S, Vt = np.linalg.svd(normalized_matrix, full_matrices=False)

# %%
# Print the shapes of U, S, and V matrices
print("Shapes of the SVD components:")
print(f"U shape: {U.shape}")
print(f"S shape: {S.shape}")
print(f"Vt shape: {Vt.shape}")

# Show some statistics about singular values
print("\nSingular values statistics:")
print(f"Number of singular values: {len(S)}")
print(f"Largest singular value: {S[0]:.4f}")
print(f"Smallest singular value: {S[-1]:.4f}")
print(f"First 10 singular values: {S[:10]}")

# %% [markdown]
# ## Question 4

# %% [markdown]
# Reconstruct four rank-k rating matrix $R_k$, where $R_k = U_kS_kV_k^T$ for k = [100, 1000, 2000, 3000]. Using each of $R_k$ make predictions for the 3 users selected in Question 1, for the movie with ID 1377 (Batman Returns). Compare the original ratings with the predicted ratings.

# %%
# First, let's recall the 3 users we selected in Question 1
print("Users selected in Question 1 who rated movie 1377 (Batman Returns):")
print(f"Selected user indices (0-based): {selected_users}")
print(f"Selected user IDs (1-based): {selected_users + 1}")

# Get the original ratings for these users for movie 1377
movie_id_1377 = 1377
movie_col_idx = movie_id_1377 - 1  # 0-indexed

print("\nOriginal ratings from the ratings_matrix:")
original_ratings = []
for user_idx in selected_users:
    user_id = user_idx + 1
    rating = ratings_matrix[user_idx, movie_col_idx]
    original_ratings.append(rating)
    print(f"User {user_id}: {rating}")

original_ratings = np.array(original_ratings)

# %%
# Define the rank values for reconstruction
k_values = [100, 1000, 2000, 3000]

# Store predictions for comparison
all_predictions = {}

print("Reconstructing rank-k approximations and making predictions...\n")
print("="*70)

for k in k_values:
    print(f"\nRank k = {k}")
    print("-" * 50)
    
    # Reconstruct the matrix using only the first k singular values
    # R_k = U_k @ S_k @ Vt_k
    U_k = U[:, :k]  # Take first k columns of U
    S_k = np.diag(S[:k])  # Create diagonal matrix with first k singular values
    Vt_k = Vt[:k, :]  # Take first k rows of Vt
    
    # Reconstruct the approximation
    R_k = U_k @ S_k @ Vt_k
    
    print(f"Reconstructed matrix R_{k} shape: {R_k.shape}")
    
    # Get predictions for the 3 selected users for movie 1377
    predictions = R_k[selected_users, movie_col_idx]
    all_predictions[k] = predictions
    
    print("\nPredictions for movie 1377 (Batman Returns):")
    for i, user_idx in enumerate(selected_users):
        user_id = user_idx + 1
        pred = predictions[i]
        orig = original_ratings[i]
        diff = pred - orig
        print(f"  User {user_id}: Predicted = {pred:.4f}, Original = {orig:.1f}, Difference = {diff:.4f}")

# %%
# Create a comparison table
print("\n" + "="*70)
print("COMPARISON TABLE: Original vs Predicted Ratings")
print("="*70)

# Header
print(f"\n{'User ID':<10} {'Original':<12}", end="")
for k in k_values:
    print(f"k={k:<6}", end="  ")
print()
print("-" * 70)

# Data rows
for i, user_idx in enumerate(selected_users):
    user_id = user_idx + 1
    print(f"{user_id:<10} {original_ratings[i]:<12.1f}", end="")
    for k in k_values:
        pred = all_predictions[k][i]
        print(f"{pred:<10.4f}", end="")
    print()

# Calculate and display average errors
print("\n" + "="*70)
print("Average Absolute Error for each k:")
print("-" * 70)
for k in k_values:
    predictions = all_predictions[k]
    mae = np.mean(np.abs(predictions - original_ratings))
    print(f"k = {k:<6}: MAE = {mae:.4f}")

print("\n" + "="*70)
print("\nObservations:")
print("- As k increases, the reconstruction becomes more accurate")
print("- Higher k values retain more information from the original matrix")
print("- The predictions approach the original (normalized) values as k increases")

# %% [markdown]
# ## Question 5

# %% [markdown]
# ### Cosine Similarity
# Cosine similarity is a metric used to measure how similar two vectors are. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. Cosine similarity is high if the angle between two vectors is 0, and the output value ranges within $cosine(x,y) \in [0,1]$. $0$ means there is no similarity (perpendicular), where $1$ (parallel) means that both the items are 100% similar.
# 
# $$ cosine(x,y) = \frac{x^T y}{||x|| ||y||}  $$

# %% [markdown]
# **Based on the reconstruction rank-1000 rating matrix $R_{1000}$ and the cosine similarity,** sort the movies which are most similar. You will have a function `top_movie_similarity` which sorts data by its similarity to a movie with ID `movie_id` and returns the top $n$ items, and a second function `print_similar_movies` which prints the titles of said similar movies. Return the top 5 movies for the movie with ID `1377` (*Batman Returns*)
# 
# Note: While finding the cosine similarity, there are a few empty columns which will have a magnitude of **zero** resulting in NaN values. These should be replaced by 0, otherwise these columns will show most similarity with the given movie. 

# %%
# First, get the rank-1000 reconstruction for use in similarity calculations
k = 1000
U_k = U[:, :k]
S_k = np.diag(S[:k])
Vt_k = Vt[:k, :]
R_1000 = U_k @ S_k @ Vt_k

print(f"Rank-1000 reconstruction matrix shape: {R_1000.shape}")

# %%
def top_movie_similarity(data, movie_id, top_n=5):
    # Convert movie_id to 0-indexed column
    movie_col_idx = movie_id - 1
    
    # Get the column for the target movie
    target_movie_vector = data[:, movie_col_idx]
    
    # Calculate cosine similarity with all movies
    # cosine(x, y) = (x^T @ y) / (||x|| * ||y||)
    
    # Compute dot products with all movie columns
    dot_products = data.T @ target_movie_vector
    
    # Compute magnitudes for all movies
    movie_magnitudes = np.linalg.norm(data, axis=0)
    target_magnitude = np.linalg.norm(target_movie_vector)
    
    # Calculate cosine similarities
    with np.errstate(divide='ignore', invalid='ignore'):
        cosine_similarities = dot_products / (movie_magnitudes * target_magnitude)
        # Replace NaN values with 0
        cosine_similarities = np.nan_to_num(cosine_similarities, nan=0.0)
    
    # Set similarity of the movie with itself to -1
    cosine_similarities[movie_col_idx] = -1
    
    # Get indices of top n most similar movies
    top_indices = np.argsort(cosine_similarities)[::-1][:top_n]
    
    return top_indices

# %%
def print_similar_movies(movie_titles, top_indices):
    print('Most Similar movies:')
    print('-' * 80)
    for i, movie_idx in enumerate(top_indices, 1):
        movie_id = movie_idx + 1
        title_row = movies_data[movies_data['MovieID'] == movie_id]
        if not title_row.empty:
            title = title_row.iloc[0]['Title']
            print(f"{i}. Movie ID {movie_id}: {title}")
        else:
            print(f"{i}. Movie ID {movie_id}: (Title not found)")

# %%
# Find and print the top 5 movies similar to Batman Returns
movie_id = 1377

batman_title = movies_data[movies_data['MovieID'] == movie_id].iloc[0]['Title']
print(f"Finding movies similar to: {batman_title} (Movie ID: {movie_id})")
print("="*80)

# Find top similar movies using rank-1000 reconstruction
top_indices = top_movie_similarity(R_1000, movie_id, top_n=5)

# Print the similar movies
print()
print_similar_movies(movies_data, top_indices)

# %% [markdown]
# ## Question 6

# %% [markdown]
# ### Movie Recommendations
# Using the same process from Question 5, write `top_user_similarity` which sorts data by its similarity to a user with ID `user_id` and returns the top result. Then find the MovieIDs of the movies that this similar user has rated most highly, but that `user_id` has not yet seen. Find at least 5 movie recommendations for the user with ID `5954` and print their titles.
# 
# Hint: To check your results, find the genres of the movies that the user likes and compare with the genres of the recommended movies.

# %%
def top_user_similarity(data, user_id):
    # Convert user_id to 0-indexed row
    user_row_idx = user_id - 1
    
    # Get the row for the target user
    target_user_vector = data[user_row_idx, :]
    
    # Calculate cosine similarity with all users
    dot_products = data @ target_user_vector
    user_magnitudes = np.linalg.norm(data, axis=1)
    target_magnitude = np.linalg.norm(target_user_vector)
    
    # Calculate cosine similarities
    with np.errstate(divide='ignore', invalid='ignore'):
        cosine_similarities = dot_products / (user_magnitudes * target_magnitude)
        cosine_similarities = np.nan_to_num(cosine_similarities, nan=0.0)
    
    # Set similarity of the user with themselves to -1
    cosine_similarities[user_row_idx] = -1
    
    # Get index of most similar user
    most_similar_user_idx = np.argmax(cosine_similarities)
    
    return most_similar_user_idx

# %%
# Find recommendations for user 5954
target_user_id = 5954
target_user_idx = target_user_id - 1

print(f"Finding movie recommendations for User ID: {target_user_id}")
print("="*80)

# Find the most similar user
similar_user_idx = top_user_similarity(R_1000, target_user_id)
similar_user_id = similar_user_idx + 1

print(f"Most similar user: User ID {similar_user_id}")

# Get movies rated by both users from original ratings matrix
target_user_ratings = ratings_matrix[target_user_idx, :]
similar_user_ratings = ratings_matrix[similar_user_idx, :]

# Find movies unseen by target user but seen by similar user
unseen_movies_mask = target_user_ratings == 0
similar_user_seen_mask = similar_user_ratings > 0
candidate_movies_mask = unseen_movies_mask & similar_user_seen_mask

# Get the ratings and sort by highest ratings
candidate_movie_indices = np.where(candidate_movies_mask)[0]
candidate_ratings = similar_user_ratings[candidate_movie_indices]
sorted_indices = np.argsort(candidate_ratings)[::-1]
top_recommendation_indices = candidate_movie_indices[sorted_indices[:5]]

print("\nTop 5 Movie Recommendations:")
print("-"*80)

for i, movie_idx in enumerate(top_recommendation_indices, 1):
    movie_id = movie_idx + 1
    rating = similar_user_ratings[movie_idx]
    movie_info = movies_data[movies_data['MovieID'] == movie_id]
    if not movie_info.empty:
        title = movie_info.iloc[0]['Title']
        genres = movie_info.iloc[0]['Genres']
        print(f"{i}. {title}")
        print(f"   Movie ID: {movie_id} | Rating: {rating} | Genres: {genres}\n")

# %%
# Analyze genres that the target user likes
print("="*80)
print(f"Genre Analysis for User {target_user_id}:")
print("-"*80)

# Get highly rated movies by target user
target_high_rated = np.where(target_user_ratings >= 4)[0]

if len(target_high_rated) > 0:
    print("\nUser's favorite movies (rated 4+):")
    for movie_idx in target_high_rated[:10]:
        movie_id = movie_idx + 1
        movie_info = movies_data[movies_data['MovieID'] == movie_id]
        if not movie_info.empty:
            title = movie_info.iloc[0]['Title']
            genres = movie_info.iloc[0]['Genres']
            print(f"- {title} | Genres: {genres}")
else:
    print("No highly rated movies found for this user.")


