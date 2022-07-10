# The LOWER attribute in the pattern describes tokens whose lowercase form matches a given value. 
#So {'LOWER': 'valley'} will match tokens like "Valley", "VALLEY", "valley" etc.

# The tokenizer already takes care of splitting off whitespace and each dictionary in the pattern describes one token.

#The tokenizer doesn't create tokens for single spaces, so there's no token with the value ' ' in between.
