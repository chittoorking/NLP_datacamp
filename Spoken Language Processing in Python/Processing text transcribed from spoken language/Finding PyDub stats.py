# You decide it'll be helpful to know the audio attributes of any given file easily. This will be especially helpful for finding out how many channels an audio file has or if the frame rate is adequate for transcription.

# In this exercise, we'll create show_pydub_stats() which takes a filename of an audio file as input. It then imports the audio as a PyDub AudioSegment instance and prints attributes such as number of channels, length and more.

# It then returns the AudioSegment instance so it can be used later on.

# We'll use our function on the newly converted .wav file, call_1.wav

# AudioSegment has already imported from PyDub.

# Instructions

# Create an AudioSegment instance called audio_segment by importing the filename parameter.
# Print the number of channels using the channels attribute.
# Return the audio_segment variable.
# Test the function on "call_1.wav".

def show_pydub_stats(filename):
  """Returns different audio attributes related to an audio file."""
  # Create AudioSegment instance
  audio_segment = AudioSegment.from_file(filename)
  
  # Print audio attributes and return AudioSegment instance
  print(f"Channels: {audio_segment.channels}")
  print(f"Sample width: {audio_segment.sample_width}")
  print(f"Frame rate (sample rate): {audio_segment.frame_rate}")
  print(f"Frame width: {audio_segment.frame_width}")
  print(f"Length (ms): {len(audio_segment)}")
  return audio_segment

# Try the function
call_1_audio_segment = show_pydub_stats('call_1.wav')
