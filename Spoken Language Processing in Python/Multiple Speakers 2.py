# Deciphering between multiple speakers in one audio file is called speaker diarization. However, you've seen the free function we've been using, recognize_google() doesn't have the ability to transcribe different speakers.

# One way around this, without using one of the paid speech to text services, is to ensure your audio files are single speaker.

# This means if you were working with phone call data, you would make sure the caller and receiver are recorded separately. Then you could transcribe each file individually.

# In this exercise, we'll transcribe each of the speakers in our multiple speakers audio file individually.

recognizer = sr.Recognizer()

# Multiple speakers on different files
speakers = [sr.AudioFile("speaker_0.wav"), 
            sr.AudioFile("speaker_1.wav"), 
            sr.AudioFile("speaker_2.wav")]

# Transcribe each speaker individually
for i, speaker in enumerate(speakers):
    with speaker as source:
        speaker_audio = recognizer.record(source)
    print(f"Text from speaker {i}:")
    print(recognizer.recognize_google(speaker_audio,
         				  language="en-US"))
