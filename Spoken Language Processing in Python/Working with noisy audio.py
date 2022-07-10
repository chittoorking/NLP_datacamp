# Let's transcribe some clean audio. Read in clean_support_call as the source and call recognize_google() on the file.

recognizer = sr.Recognizer()

# Record the audio from the clean support call
with clean_support_call as source:
  clean_support_call_audio = recognizer.record(source)

# Transcribe the speech from the clean support call
text = recognizer.recognize_google(clean_support_call_audio,
					   language="en-US")

print(text)


# Let's do the same as before but with a noisy audio file saved as noisy_support_call and show_all parameter as True.
recognizer = sr.Recognizer()

# Record the audio from the noisy support call
with noisy_support_call as source:
  noisy_support_call_audio = recognizer.record(source)

# Transcribe the speech from the noisy support call
text = recognizer.recognize_google(noisy_support_call_audio,
                         language="en-US",
                         show_all=True)

print(text)
# Set the duration parameter of adjust_for_ambient_noise() to 1 (second) so recognizer adjusts for background noise.

recognizer = sr.Recognizer()

# Record the audio from the noisy support call
with noisy_support_call as source:
	# Adjust the recognizer energy threshold for ambient noise
    recognizer.adjust_for_ambient_noise(source, duration=1.0)
    noisy_support_call_audio = recognizer.record(noisy_support_call)
 
# Transcribe the speech from the noisy support call
text = recognizer.recognize_google(noisy_support_call_audio,
                                   language="en-US",
                                   show_all=True)

print(text)

# A duration of 1 was too long and it cut off some of the audio. Try setting duration to 0.5.

recognizer = sr.Recognizer()

# Record the audio from the noisy support call
with noisy_support_call as source:
	# Adjust the recognizer energy threshold for ambient noise
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    noisy_support_call_audio = recognizer.record(noisy_support_call)
 
# Transcribe the speech from the noisy support call
text = recognizer.recognize_google(noisy_support_call_audio,
                                   language="en-US",
                                   show_all=True)

print(text)
