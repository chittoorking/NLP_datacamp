# Let's use the match patterns we've created in the previous exercise to bootstrap a set of training examples. The nlp object has already been created for you and the Matcher with the added patterns pattern1 and pattern2 is available as the variable matcher. A list of sentences is available as the variable TEXTS.

# Instructions 
# Create a doc object for each text using nlp.pipe and find the matches in it.
# Create a list of (start, end, label) tuples for the matches.

# Create a Doc object for each text in TEXTS
for doc in list(nlp.pipe(TEXTS)):
    # Find the matches in the doc
    matches = matcher(doc)
    
    # Get a list of (start, end, label) tuples of matches in the text
    entities = [(start, end, 'GADGET') for x, start, end in matches]
    print(doc.text, entities)    
    
#     Match on the doc and create a list of matched spans.
# Format each example as a tuple of the text and a dict, mapping 'entities' to the entity tuples.
# Append the example to TRAINING_DATA and inspect the printed data.

TRAINING_DATA = []

# Create a Doc object for each text in TEXTS
for doc in nlp.pipe(TEXTS):
    # Match on the doc and create a list of matched spans
    spans = [doc[start:end] for match_id, start, end in matcher(doc)]
    # Get (start character, end character, label) tuples of matches
    entities = [(span.start_char, span.end_char, 'GADGET') for span in spans]
    
    # Format the matches as a (doc.text, entities) tuple
    training_example = (doc.text, {'entities': entities})
    # Append the example to the training data
    TRAINING_DATA.append(training_example)
    
print(*TRAINING_DATA, sep='\n')    



# ('How to preorder the iPhone X', {'entities': [(20, 28, 'GADGET')]})
# ('iPhone X is coming', {'entities': [(0, 8, 'GADGET')]})
# ('Should I pay $1,000 for the iPhone X?', {'entities': [(28, 36, 'GADGET')]})
# ('The iPhone 8 reviews are here', {'entities': [(4, 12, 'GADGET')]})
# ('Your iPhone goes up to 11 today', {'entities': []})
# ('I need a new phone! Any tips?', {'entities': []})
