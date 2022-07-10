# Rewrite the example to use nlp.pipe. Instead of iterating over the texts and processing them, iterate over the doc objects yielded by nlp.pipe.


# Incorrect Submission
# Check the first for loop. Did you correctly specify the iterable part? Expected nlp.pipe(TEXTS), but got list(nlp.pipe(TEXTS)).
# Did you find this feedback helpful?
#2
# Rewrite the example to use nlp.pipe. Don't forget to call list() around the result to turn it into a list.
# 3
# Rewrite the example to use nlp.pipe. Don't forget to call list() around the result to turn it into a list.



# Process the texts and print the adjectives
for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == 'ADJ'])


# Process the texts and print the entities
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)

people = ['David Bowie', 'Angela Merkel', 'Lady Gaga']

# Create a list of patterns for the PhraseMatcher
patterns = list(nlp.pipe(people))
