# Alright, now you've got functions to convert audio files and find out their attributes, it's time to build one to transcribe them.

# In this exercise, you'll build transcribe_audio() which takes a filename as input, imports the filename using speech_recognition's AudioFile class and then transcribes it using recognize_google().

# You've seen these functions before but now we'll put them together so they're accessible in a function.

# To test it out, we'll transcribe Acme's first call, "call_1.wav".

# speech_recognition has been imported as sr.

# Instructions
# Define a function called transcribe_audio which takes filename as an input parameter.
# Setup a Recognizer() instance as recognizer.
# Use recognize_google() to transcribe the audio data.
# Pass the target call to the function.



def transcribe_audio(filename):
  """Takes a .wav format audio file and transcribes it to text."""
  # Setup a recognizer instance
  recognizer = sr.Recognizer()
  
  # Import the audio file and convert to audio data
  audio_file = sr.AudioFile(filename)
  with audio_file as source:
    audio_data = recognizer.record(source)
  
  # Return the transcribed text
  return recognizer.recognize_google(audio_data)

# Test the function
print(transcribe_audio('call_1.wav'))
