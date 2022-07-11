# Acme Studios have asked you to do a proof of concept to find out more about their audio files.

# After exploring them briefly, you find there's a few calls but they're in the wrong file format for transcription.

# As you'll be interacting with many audio files, you decide to begin by creating some helper functions.

# The first one, convert_to_wav(filename) takes a file path and uses PyDub to convert it from a non-wav format to .wav format.

# Once it's built, we'll use the function to convert Acme's first call, call_1.mp3, from .mp3 format to .wav.

# PyDub's AudioSegment class has already been imported. Remember, to work with non-wav files, you'll need ffmpeg.

# Instructions

# Import the filename parameter using AudioSegment's from_file().
# Set the export format to "wav".
# Pass the target audio file, call_1.mp3, to the function.

# Create function to convert audio file to wav
def convert_to_wav(filename):
  """Takes an audio file of non .wav format and converts to .wav"""
  # Import audio file
  audio = AudioSegment.from_file(filename)
  
  # Create new filename
  new_filename = filename.split(".")[0] + ".wav"
  
  # Export file as .wav
  audio.export(new_filename, format='wav')
  print(f"Converting {filename} to {new_filename}...")
 
# Test the function
convert_to_wav('call_1.mp3')
