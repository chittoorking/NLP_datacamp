# You've seen how there are different kinds of audio files and how streaming music and spoken language have different sampling rates. But now we want to start working with these files.

# To begin, we're going to import the good_morning.wav audio file using Python's in-built wave library. Then we'll see what it looks like in byte form using the built-in readframes() method.

# You can listen to good_morning.wav here.

# Remember, good_morning.wav is only a few seconds long but at 48 kHz, that means it contains 48,000 pieces of information per second.

# Instructions

# Import the Python wave library.
# Read in the good_morning.wav audio file and save it to good_morning.
# Create signal_gm by reading all the frames from good_morning using readframes().
# See what the first 10 frames of audio look like by slicing signal_gm.

import wave

# Create audio file wave object
good_morning = wave.open('good_morning.wav', 'r')

# Read all frames from wave object 
signal_gm = good_morning.readframes(-1)

# View first 10
print(signal_gm[:10])
