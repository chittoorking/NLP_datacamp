# Let's try setting some more complex attributes using getters and method extensions. The nlp object has already been created for you and the Doc, Token and Span classes are already imported.

# Remember that if you run your code more than once, you might see an error message that the extension already exists. That's because DataCamp will re-run your code in the same session. To solve this, you can set force=True on set_extension, or reload to start a new Python session. None of this will affect the answer you submit.

# Instructions 1/2
# Complete the has_number function .
# Use Doc.set_extension to register 'has_number' (getter get_has_number) and print its value.



# Define the getter function
def get_has_number(doc):
    # Return if any of the tokens in the doc return True for token.like_num
    return any(token.like_num for token in doc)

# Register the Doc property extension 'has_number' with the getter get_has_number
Doc.set_extension("has_number", getter=get_has_number,force=True)

# Process the text and check the custom has_number attribute 
doc = nlp("The museum closed for five years in 2012.")
print('has_number:', doc._.has_number)


# Use Span.set_extension to register 'to_html' (method to_html).
# Call it on doc[0:2] with the tag 'strong'.

# Define the method
def to_html(span, tag):
    # Wrap the span text in a HTML tag and return it
    return '<{tag}>{text}</{tag}>'.format(tag=tag, text=span.text)

# Register the Span property extension 'to_html' with the method to_html
Span.set_extension('to_html', method=to_html)

# Process the text and call the to_html method on the span with the tag name 'strong'
doc = nlp("Hello world, this is a sentence.")
span = doc[0:2]
print(span._.to_html('strong'))
