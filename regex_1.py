#Split my_string on each sentence ending. 
#To do this:
#Write a pattern called sentence_endings to match sentence endings (.?!).
#Use re.split() to split my_string on the pattern and print the result.
#Find and print all capitalized words in my_string by writing a pattern called capitalized_words and using re.findall().
#Remember the [a-z] pattern shown in the video to match lowercase groups? Modify that pattern appropriately in order to match uppercase groups.
#Write a pattern called spaces to match one or more spaces ("\s+") and then use re.split() to split my_string on this pattern, keeping all punctuation intact. Print the result.
#Find all digits in my_string by writing a pattern called digits ("\d+") and using re.findall(). Print the result.
# Write a pattern to match sentence endings: sentence_endings
my_string="Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"

sentence_endings = r"[.?!]"

# Split my_string on sentence endings and print the result
print(re.split(sentence_endings,my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words,my_string))

# Split my_string on spaces and print the result
spaces = r"\s+"
print(re.split(spaces,my_string))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, my_string))
#["Let's write RegEx", "  Won't that be fun", '  I sure think so', '  Can you find 4 sentences', '  Or perhaps, all 19 words', '']
#['Let', 'RegEx', 'Won', 'Can', 'Or']
#["Let's", 'write', 'RegEx!', "Won't", 'that', 'be', 'fun?', 'I', 'sure', 'think', 'so.', 'Can', 'you', 'find', '4', 'sentences?', 'Or', 'perhaps,', 'all', '19', 'words?']
#['4', '19']
