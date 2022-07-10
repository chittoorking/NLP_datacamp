# Pass the Japanese version of good morning (japanese_audio) to recognize_google() using "en-US" as the language.

# Pass the same Japanese audio (japanese_audio) using "ja" as the language parameter. Do you see a difference?

# What about about non-speech audio? Pass leopard_audio to recognize_google() with show_all as True.

# What if your speech files have non-audible human sounds? Pass charlie_audio to recognize_google() to find out.


# Create a recognizer class
recognizer = sr.Recognizer()

# Pass the Japanese audio to recognize_google
text = recognizer.recognize_google(japanese_audio, language='en-US')

# Print the text
print(text)




# Create a recognizer class
recognizer = sr.Recognizer()

# Pass the Japanese audio to recognize_google
text = recognizer.recognize_google(japanese_audio, language='ja')

# Print the text
print(text)

# Create a recognizer class
recognizer = sr.Recognizer()

# Pass the leopard roar audio to recognize_google
text = recognizer.recognize_google(leopard_audio, 
                                   language="en-US", 
                                   show_all=True)

# Print the text
print(text)



# Create a recognizer class
recognizer = sr.Recognizer()

# Pass charlie_audio to recognize_google
text = recognizer.recognize_google(charlie_audio, 
                                   language="en-US")

# Print the text
print(text)
