# Let's write a simple training loop from scratch!

# The pipeline you've created in the previous exercise is available as the nlp object. It already contains the entity recognizer with the added label 'GADGET'.

# The small set of labelled examples that you've created previously is available as the global variable TRAINING_DATA. To see the examples, you can print them in your script or in the IPython shell. spacy and random have already been imported for you.
# Start the training
nlp.begin_training()

# Loop for 10 iterations
for itn in range(10):
    # Shuffle the training data
    random.shuffle(TRAINING_DATA)
    losses = {}
    
    # Batch the examples and iterate over them
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]
        
        # Update the model
        nlp.update(texts, annotations, losses=losses)
        print(losses)
