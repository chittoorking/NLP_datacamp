# During your exploratory data analysis, you may find some of the parameters of your audio files differ or are incompatible with speech recognition APIs.

# Don't worry, PyDub has built-in functionality which allows you to change various attributes.

# For example, you can set the frame rate of your audio file calling set_frame_rate() on your AudioSegment instance and passing it an integer of the desired frame rate measured in Hertz.

# In this exercise, we'll practice altering some audio attributes.

# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Create a new wav file with adjusted frame rate
wav_file_16k = wav_file.set_frame_rate(16000)

# Check the frame rate of the new wav file
print(wav_file_16k.frame_rate)

# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Set number of channels to 1
wav_file_1_ch = wav_file.set_channels(1)

# Check the number of channels
print(wav_file_1_ch.channels)

# Import audio file
wav_file = AudioSegment.from_file(file="wav_file.wav")

# Print sample_width
print(f"Old sample width: {wav_file.sample_width}")

# Set sample_width to 1
wav_file_sw_1 = wav_file.set_sample_width(1)

# Check new sample_width
print(f"New sample width: {wav_file_sw_1.sample_width}")
