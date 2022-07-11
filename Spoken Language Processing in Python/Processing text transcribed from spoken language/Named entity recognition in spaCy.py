# Named entities are real-world objects which have names, such as, cities, people, dates or times. We can use spaCy to find named entities in our transcribed text.

# In this exercise, you'll transcribe call_4_channel_2.wav using transcribe_audio() and then use spaCy's language model, en_core_web_sm to convert the transcribed text to a spaCy doc.

# Transforming text to a spaCy doc allows us to leverage spaCy's built-in features for analyzing text, such as, .text for tokens (single words), .sents for sentences and .ents for named entities.

# Instructions 
# Create a spaCy doc by passing the transcribed call 4 channel 2 text to nlp() and then check its type.

import spacy

# Transcribe call 4 channel 2
call_4_channel_2_text = transcribe_audio("call_4_channel_2.wav")

# Create a spaCy language model instance
nlp = spacy.load("en_core_web_sm")

# Create a spaCy doc with call 4 channel 2 text
doc = nlp('call_4_channel_2')

# Check the type of doc
print(type(doc))

# Create a spaCy doc with call_4_channel_2_text then print all the token text in it using the .text attribute.

import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Create a spaCy doc with call 4 channel 2 text
doc = nlp(call_4_channel_2_text)

# Show tokens in doc
for token in doc:
    print(token.text, token.idx)
    
    
# Load the "en_core_web_sm" language model and then print the sentences in the doc using the .sents attribute.

import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Create a spaCy doc with call 4 channel 2 text
doc = nlp(call_4_channel_2_text)

# Show sentences in doc
for sentence in doc.sents:
    print(sentence)
# Access the entities in the doc using .ents and then print the text of each.
import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Create a spaCy doc with call 4 channel 2 text
doc = nlp(call_4_channel_2_text)

# Show named entities and their labels
for entity in doc.ents:
    print(entity.text, entity.label_)
