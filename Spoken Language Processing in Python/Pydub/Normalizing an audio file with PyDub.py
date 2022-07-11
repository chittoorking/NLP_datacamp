# Sometimes you'll have audio files where the speech is loud in some portions and quiet in others. Having this variance in volume can hinder transcription.

# Luckily, PyDub's effects module has a function called normalize() which finds the maximum volume of an AudioSegment, then adjusts the rest of the AudioSegment to be in proportion. This means the quiet parts will get a volume boost.

# You can listen to an example of an audio file which starts as loud then goes quiet, loud_then_quiet.wav, here.

# In this exercise, you'll use normalize() to normalize the volume of our file, making it sound more like this.

# Instructions
# Import AudioSegment from PyDub and normalize from the PyDub's effects module.
# Import the target audio file, loud_then_quiet.wav and save it to loud_then_quiet.
# Normalize the imported audio file using the normalize() function and save it to normalized_loud_then_quiet.

# Import AudioSegment and normalize
from pydub import AudioSegment
from pydub.effects import normalize

# Import target audio file
loud_then_quiet = AudioSegment.from_file('loud_then_quiet.wav')

# Normalize target audio file
normalized_loud_then_quiet = normalize(loud_then_quiet)
