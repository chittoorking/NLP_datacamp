# In this exercise, you'll combine custom extension attributes with the model's predictions and create an attribute getter that returns a Wikipedia search URL if the span is a person, organization, or location.

# The Span class is already imported and the nlp object has been created for you.

# Instructions
# Complete the get_wikipedia_url getter so it only returns the URL if the span's label is in the list of labels.
# Set the Span extension 'wikipedia_url' using the getter get_wikipedia_url.
# Iterate over the entities in the doc and output their Wikipedia URL.

def get_wikipedia_url(span):
    # Get a Wikipedia URL if the span has one of the labels
    if span.label_ in ('PERSON', 'ORG', 'GPE', 'LOCATION'):
        entity_text = span.text.replace(' ', '_')
        return "https://en.wikipedia.org/w/index.php?search=" + entity_text

# Set the Span extension wikipedia_url using get getter get_wikipedia_url
Span.set_extension('wikipedia_url', getter=get_wikipedia_url,force=True)

doc = nlp("In over fifty years from his very first recordings right through to his last album, David Bowie was at the vanguard of contemporary culture.")
for ent in doc.ents:
    # Print the text and Wikipedia URL of the entity
    print(ent.text, ent._.wikipedia_url)
