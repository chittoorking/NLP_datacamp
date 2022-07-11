# Okay, now we've got some helper functions ready to go, it's time to put them to use!

# You'll first use convert_to_wav() to convert Acme's call_1.mp3 to .wav format and save it as call_1.wav

# Using show_pydub_stats() you find call_1.wav has 2 channels so you decide to split them using PyDub's split_to_mono(). Acme tells you the customer channel is likely channel 2. So you export channel 2 using PyDub's .export().

# Finally, you'll use transcribe_audio() to transcribe channel 2 only.

# Instructions 
# Convert the .mp3 version of call_1 to .wav and then check the stats of the .wav version.

# Convert mp3 file to wav
convert_to_wav('call_1.mp3')

# Check the stats of new file
call_1 = show_pydub_stats('call_1.wav')

# Split call_1 to mono and then export the second channel in .wav format.
# Convert mp3 file to wav
convert_to_wav("call_1.mp3")

# Check the stats of new file
call_1 = show_pydub_stats("call_1.wav")

# Split call_1 to mono
call_1_split = call_1.split_to_mono()

# Export channel 2 (the customer channel)
call_1_split[1].export("call_1_channel_2.wav",
                       format='wav')

# Transcribe the audio of call 1's channel 2.
# Transcribe the single channel
print(transcribe_audio('call_1_channel_2.wav'))
