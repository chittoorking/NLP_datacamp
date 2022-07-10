# Sometimes it's more efficient to match exact strings instead of writing patterns describing the individual tokens. This is especially true for finite categories of things – like all countries of the world.

# We already have a list of countries, so let's use this as the basis of our information extraction script. A list of string names is available as the variable COUNTRIES. The nlp object and a test doc have already been created and the doc.text has been printed to the shell.

# Instructions
# Import the PhraseMatcher and initialize it with the shared vocab as the variable matcher.
# Add the phrase patterns and call the matcher on the doc.

# Import the PhraseMatcher and initialize it
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)

# Create pattern Doc objects and add them to the matcher
# This is the faster version of: [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add('COUNTRY', None, *patterns)

# Call the matcher on the test document and print the result
matches = matcher(doc)
print([doc[start:end] for match_id, start, end in matches])
