#The code in this example is trying to analyze a text and collect all proper nouns.
#If the token following the proper noun is a verb, it should also be extracted. A doc object has already been created.


# Get all tokens and part-of-speech tags
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Check if the current token is a proper noun
    if pos == 'PROPN':
        # Check if the next token is a verb
        if pos_tags[index + 1] == 'VERB':
            print('Found a verb after a proper noun!')
