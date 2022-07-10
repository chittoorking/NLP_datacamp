# Let's inspect the small English model's pipeline!

# Instructions
# Load the en_core_web_sm model and create the nlp object.
# Print the names of the pipeline components using nlp.pipe_names.
# Print the full pipeline of (name, component) tuples using nlp.pipeline.

# Load the en_core_web_sm model
nlp = spacy.load("en_core_web_sm")

# Print the names of the pipeline components
print(nlp.pipe_names)

# Print the full pipeline of (name, component) tuples
print(nlp.pipeline)

# ['tagger', 'parser', 'ner']
# [('tagger', <spacy.pipeline.pipes.Tagger object at 0x7f51b2578828>), ('parser', <spacy.pipeline.pipes.DependencyParser object at 0x7f51b24a1e28>), ('ner', <spacy.pipeline.pipes.EntityRecognizer object at 0x7f51b24a1e88>)]
