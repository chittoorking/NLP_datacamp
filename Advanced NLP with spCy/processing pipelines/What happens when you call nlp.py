# Correct! The tokenizer turns a string of text into a Doc object. spaCy then applies every component in the pipeline on document, in order.

What does spaCy do when you call nlp on a string of text? The IPython shell has a pre-loaded nlp object that logs what's going on under the hood. Try processing a text with it!

doc = nlp("This is a sentence.")
