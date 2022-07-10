# If your goal is to transcribe conversations, there will be more than one speaker. However, as you'll see, the recognize_google() function will only transcribe speech into a single block of text.

# You can hear in this audio file there are three different speakers.

# But if you transcribe it on its own, recognize_google() returns a single block of text. Which is still useful but it doesn't let you know which speaker said what.

# We'll see an alternative to this in the next exercise.

# The multiple speakers audio file has been imported and converted to AudioData as multiple_speakers.


# Create a recognizer class
recognizer = sr.Recognizer()

# Recognize the multiple speaker AudioData
text = recognizer.recognize_google(multiple_speakers, 
                       			   language='en-US')

# Print the text
print(text)
