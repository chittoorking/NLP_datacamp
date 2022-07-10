# In this exercise, you'll prepare a spaCy pipeline to train the entity recognizer to recognize 'GADGET' entities in a text – for exampe, "iPhone X".

# spacy has already been imported for you.

# Create a blank 'en' model
nlp = spacy.blank('en')

# Create a new entity recognizer and add it to the pipeline
ner = nlp.create_pipe('ner')
nlp.add_pipe(ner)

# Add the label 'GADGET' to the entity recognizer
ner.add_label('GADGET')

