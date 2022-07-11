# Now you've transcribed some customer call audio data, we'll build a model to classify whether the text from the customer call is pre_purchase or post_purchase.

# We've got 45 examples of pre_purchase calls and 57 examples of post_purchase calls.

# The data the model will train on is stored in train_df and the data the model will predict on is stored in test_df.

# Try printing the .head() of each of these to the console.

# We'll build an sklearn pipeline using CountVectorizer() and TfidfTransformer() to convert our text samples to numbers and then use a MultinomialNB() classifier to learn what category each sample belongs to.

# This model will work well on our small example here but for larger amounts of text, you may want to consider something more sophisticated.

# Create text_classifier using CountVectorizer(), TfidfTransformer(), and MultinomialNB().
# Fit text_classifier on train_df.text and train_df.label.

# Build the text_classifier as an sklearn pipeline
text_classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])

# Fit the classifier pipeline on the training data
text_classifier.fit(train_df.text, train_df.label)

# Create predicted by calling predict() on text_classifier and passing it the text column of test_df.
# Evaluate the model by seeing how predicted compares to the test_df.label.

# Build the text_classifier as an sklearn pipeline
text_classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])

# Fit the classifier pipeline on the training data
text_classifier.fit(train_df.text, train_df.label)

# Evaluate the MultinomialNB model
predicted = text_classifier.predict(test_df.text)
accuracy = 100 * np.mean(predicted == test_df.label)
print(f'The model is {accuracy}% accurate')
