# Load the en_core_web_sm model
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp(loft)

# Generate tokens and pos tags
pos = [(token.text, token.pos_) for token in doc]
print(pos)
