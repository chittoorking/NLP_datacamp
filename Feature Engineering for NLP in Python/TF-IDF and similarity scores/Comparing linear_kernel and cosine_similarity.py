# Record start time
start = time.time()

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Print cosine similarity matrix
print(cosine_sim)

# Print time taken
print("Time taken: %s seconds" %(time.time() - start))

# [[1.         0.         0.         ... 0.         0.         0.        ]
#  [0.         1.         0.         ... 0.         0.         0.        ]
#  [0.         0.         1.         ... 0.         0.01418221 0.        ]
#  ...
#  [0.         0.         0.         ... 1.         0.01589009 0.        ]
#  [0.         0.         0.01418221 ... 0.01589009 1.         0.        ]
#  [0.         0.         0.         ... 0.         0.         1.        ]]
# Time taken: 0.3812108039855957 seconds


# Record start time
start = time.time()

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Print cosine similarity matrix
print(cosine_sim)

# Print time taken
print("Time taken: %s seconds" %(time.time() - start))
# [[1.         0.         0.         ... 0.         0.         0.        ]
#  [0.         1.         0.         ... 0.         0.         0.        ]
#  [0.         0.         1.         ... 0.         0.01418221 0.        ]
#  ...
#  [0.         0.         0.         ... 1.         0.01589009 0.        ]
#  [0.         0.         0.01418221 ... 0.01589009 1.         0.        ]
#  [0.         0.         0.         ... 0.         0.         1.        ]]
# Time taken: 0.3082237243652344 seconds
