# Create the doc object
doc = nlp(sent)

# Compute pairwise similarity scores
for token1 in doc:
  for token2 in doc:
    print(token1.text, token2.text, token1.similarity(token2))
    
# I I 1.0
# I like 0.13463904
# I apples -0.03613354
# I and -0.08523061
# I oranges 0.033708718
# like I 0.13463904
# like like 1.0
# like apples 0.0007652738
# like and 0.10452179
# like oranges -0.045859177
# apples I -0.03613354
# apples like 0.0007652738
# apples apples 1.0
# apples and -0.051073108
# apples oranges 0.46451995
# and I -0.08523061
# and like 0.10452179
# and apples -0.051073108
# and and 1.0
# and oranges 0.03823666
# oranges I 0.033708718
# oranges like -0.045859177
# oranges apples 0.46451995
# oranges and 0.03823666
# oranges oranges 1.0
