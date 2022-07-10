# Now you've created an instance of the Recognizer class we'll use the recognize_google() method on it to access the Google web speech API and turn spoken language into text.

# recognize_google() requires an argument audio_data otherwise it will return an error.

# US English is the default language. If your audio file isn't in US English, you can change the language with the language argument. A list of language codes can be seen here.

# An audio file containing English speech has been imported as clean_support_call_audio. You can listen to the audio file here. SpeechRecognition has also been imported as sr.

# To avoid hitting the API request limit of Google's web API, we've mocked the Recognizer class to work with our audio files. This means some functionality will be limited.

# Instructions
# Call the recognize_google() method on recognizer and pass it clean_support_call_audio.
# Set the language argument to "en-US".

# Create a recognizer class
recognizer = sr.Recognizer()

# Transcribe the support call audio
text = recognizer.recognize_google(
  audio_data=clean_support_call_audio, 
  language='en-US')

print(text)
