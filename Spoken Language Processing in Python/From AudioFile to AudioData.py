# As you saw earlier, there are some transformation steps we have to take to make our audio data useful. The same goes for SpeechRecognition.

# In this exercise, we'll import the clean_support_call.wav audio file and get it ready to be recognized.

# We first read our audio file using the AudioFile class. But the recognize_google() method requires an input of type AudioData.

# To convert our AudioFile to AudioData, we'll use the Recognizer class's method record() along with a context manager. The record() method takes an AudioFile as input and converts it to AudioData, ready to be used with recognize_google().

# SpeechRecognition has already been imported as sr.

# Instructions
# Pass the AudioFile class clean_support_call.wav.
# Use the context manager to open and read clean_support_call as source.
# Record source and run the code.

# Instantiate Recognizer
recognizer = sr.Recognizer()

# Convert audio to AudioFile
clean_support_call = sr.AudioFile('clean_support_call.wav')

# Convert AudioFile to AudioData
with clean_support_call as source:
    clean_support_call_audio = recognizer.record(source)

# Transcribe AudioData to text
text = recognizer.recognize_google(clean_support_call_audio,
                                   language="en-US")
print(text)
