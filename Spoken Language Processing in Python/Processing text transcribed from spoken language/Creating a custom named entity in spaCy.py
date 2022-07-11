# If spaCy's built-in named entities aren't enough, you can make your own using spaCy's EntityRuler() class.

# EntityRuler() allows you to create your own entities to add to a spaCy pipeline.

# You start by creating an instance of EntityRuler() and passing it the current pipeline, nlp.

# You can then call add_patterns() on the instance and pass it a dictionary of the text pattern you'd like to label with an entity.

# Once you've setup a pattern you can add it the nlp pipeline using add_pipe().

# Since Acme is a technology company, you decide to tag the pattern "smartphone" with the "PRODUCT" entity tag.

# spaCy has been imported and a doc already exists containing the transcribed text from call_4_channel_2.wav.

# Instructions
# Import EntityRuler from spacy.pipeline.
# Add "smartphone" as the value for the "pattern" key.
# Add the EntityRuler() instance, ruler, to the nlp pipeline.
# Print the entity attributes contained in doc.

# Import EntityRuler class
from spacy.pipeline import EntityRuler

# Create EntityRuler instance
ruler = EntityRuler(nlp)

# Define pattern for new entity
ruler.add_patterns([{"label": "PRODUCT", "pattern": 'smartphone'}])

# Update existing pipeline
nlp.add_pipe(ruler, before="ner")

# Test new entity
for entity in doc.ents:
  print(entity.text, entity.label_)
