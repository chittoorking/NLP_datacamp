# Convert the sound wave bytes to integers.
# Get the frame rate of the good morning audio file using getframerate().
# Set stop to be the length of soundwave_gm over the frame rate.
# Set num to be the length of soundwave_gm.

# Read in sound wave and convert from bytes to integers
good_morning = wave.open('good_morning.wav', 'r')
signal_gm = good_morning.readframes(-1)
soundwave_gm = np.frombuffer(signal_gm, dtype='int16')

# Get the sound wave frame rate
framerate_gm = good_morning.getframerate()

# Find the sound wave timestamps
time_gm = np.linspace(start=0,
                      stop=len(soundwave_gm)/framerate_gm,
					  num=len(soundwave_gm))

# Print the first 10 timestamps
print(time_gm[:10])
