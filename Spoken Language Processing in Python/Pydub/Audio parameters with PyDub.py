# Every audio file you work with will have a number of characteristics associated with them, such as, channels, frame rate (or sample rate), sample width and more.

# Knowing these parameters is useful to ensure your audio files are compatible with various API requirements for speech transcription.

# For example, many APIs recommend a minimum frame rate (wav_file.frame_rate) of 16,000 Hz.

# When you create an instance of AudioSegment, PyDub automatically infers these parameters from your audio files and saves them as attributes.

# In this exercise, we'll explore these attributes.

# Instructions 
# Find the frame_rate of wav_file.

# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the frame rate
print(wav_file.frame_rate)

# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the number of channels
print(wav_file.channels)

# Find the max amplitude of wav_file.

# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the max amplitude
print(wav_file.max)

# Find the length of wav_file in milliseconds.
# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Find the length
print(len(wav_file))
