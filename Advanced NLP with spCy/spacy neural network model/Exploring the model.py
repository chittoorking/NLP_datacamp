# Let's see how the model performs on unseen data! To speed things up a little, here's a trained model for the label 'GADGET',
# using the examples from the previous exercise, plus a few hundred more. The loaded model is already available as the nlp object. 
# A list of test texts is available as TEST_DATA.


# Process each text in TEST_DATA
for doc in nlp.pipe(TEST_DATA):
    # Print the document text and entitites
    print(doc.text)
    print(doc.ents, '\n\n')
