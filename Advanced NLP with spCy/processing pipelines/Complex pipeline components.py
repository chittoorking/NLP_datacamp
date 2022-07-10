# In this exercise, you'll be writing a custom component that uses the PhraseMatcher to find animal names in the document and adds the matched spans to the doc.ents.

# A PhraseMatcher with the animal patterns has already been created as the variable matcher. The small English model is available as the variable nlp. The Span object has already been imported for you.

# Instructions 1/3
# Define the custom component and apply the matcher to the doc.
# Create a Span for each match, assign the label ID for 'ANIMAL' and overwrite the doc.ents with the new spans.

# Define the custom component
def animal_component(doc):
    # Apply the matcher to the doc
    matches = matcher(doc)
    # Create a Span for each match and assign the label 'ANIMAL'
    spans = [Span(doc, start, end, label="ANIMAL")
             for match_id, start, end in matches]
    # Overwrite the doc.ents with the matched spans
    doc.ents = spans
    return doc
  
# Add the component to the pipeline after the 'ner' component 
nlp.add_pipe(animal_component, after='ner')
print(nlp.pipe_names)

# animal_patterns: [Golden Retriever, cat, turtle, Rattus norvegicus]

# Process the text and print the entity text and entity label for the entities in doc.ents.

# Process the text and print the text and label for the doc.ents
doc = nlp("I have a cat and a Golden Retriever")
print([(ent.text, ent.label_) for ent in doc.ents])
