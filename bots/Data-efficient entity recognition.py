# Most systems for extracting entities from text are built to extract 'Universal' things like names, dates, and places. But you probably don't have enough training data for your bot to make these systems perform well!

# In this exercise, you'll activate the MITIE entity recognizer inside Rasa to extract restaurants-related entities using a very small amount of training data. A dictionary args has already been defined for you, along with a training_data object.
# Import necessary modules
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

pipeline = [
    "nlp_spacy",
    "tokenizer_spacy",
    "ner_crf"
]

# Create a config that uses this pipeline
config = RasaNLUConfig(cmdline_args={"pipeline":pipeline})

# Create a trainer that uses this config
trainer = Trainer(config)

# Create an interpreter by training the model
interpreter = trainer.train(training_data)

# Parse some messages
print(interpreter.parse("show me Chinese food in the centre of town"))
print(interpreter.parse("I want an Indian restaurant in the west"))
print(interpreter.parse("are there any good pizza places in the center?"))
