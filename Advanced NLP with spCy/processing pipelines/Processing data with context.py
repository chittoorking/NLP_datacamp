# In this exercise, you'll be using custom attributes to add author and book meta information to quotes.

# A list of (text, context) examples is available as the variable DATA. The texts are quotes from famous books, and the contexts dictionaries with the keys 'author' and 'book'. The nlp object has already been created for you.

# Instructions 
# Import the Doc class and use the set_extension method to register the custom attributes 'author' and 'book', which default to None.
# Process the (text, context) tuples in DATA using nlp.pipe with as_tuples=True.
# Overwrite the doc._.book and doc._.author with the respective info passed in as the context.

# Import the Doc class
from spacy.tokens import Doc

# Register the Doc extension 'author' (default None)
Doc.set_extension('author',default=None)

# Register the Doc extension 'book' (default None)
Doc.set_extension('book',default=None)


# Import the Doc class and register the extensions 'author' and 'book'
from spacy.tokens import Doc
Doc.set_extension('book', default=None)
Doc.set_extension('author', default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # Set the doc._.book and doc._.author attributes from the context
    doc._.book = context['book']
    doc._.author = context['author']
    
    # Print the text and custom attribute data
    print(doc.text, '\n', "— '{}' by {}".format(doc._.book, doc._.author), '\n')

    
    
#The same technique is useful for a variety of tasks. For example, you could pass in page or paragraph numbers to relate the processed Doc back to the position in a larger document.
# Or you could pass in other structured data like IDs referring to a knowledge base.
