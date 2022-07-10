# Let's transcribe some clean audio. Read in clean_support_call as the source and call recognize_google() on the file.

recognizer = sr.Recognizer()

# Record the audio from the clean support call
with clean_support_call as source:
  clean_support_call_audio = recognizer.record(source)

# Transcribe the speech from the clean support call
text = recognizer.recognize_google(clean_support_call_audio,
					   language="en-US")

print(text)
