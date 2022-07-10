# spaCy's rule-based Matcher is a great way to quickly create training data for named entity models. A list of sentences is available as the variable TEXTS. You can print it the IPython shell to inspect it. We want to find all mentions of different iPhone models, so we can create training data to teach a model to recognize them as 'GADGET'.

# The nlp object has already been created for you and the Matcher is available as the variable matcher.

# Instructions
# Write a pattern for two tokens whose lowercase forms match 'iphone' and 'x'.
# Write a pattern for two tokens: one token whose lowercase form matches 'iphone' and an optional digit using the '?' operator.


# Two tokens whose lowercase forms match 'iphone' and 'x'
pattern1 = [{'LOWER': 'iphone'}, {'LOWER': 'x'}]

# Token whose lowercase form matches 'iphone' and an optional digit
pattern2 = [{'LOWER': 'iphone'}, {'IS_DIGIT':True , 'OP': '?'}]

# Add patterns to the matcher
matcher.add('GADGET', None, pattern1, pattern2)
