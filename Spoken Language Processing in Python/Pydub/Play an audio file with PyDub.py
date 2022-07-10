# If you're working with audio files, chances are you want to listen to them.

# PyDub's playback module provides a function called play() which can be passed an AudioSegment. Running the play() function with an AudioSegment passed in will play the AudioSegment out loud.

# This can be helpful to check the quality of your audio files and assess any changes you need to make.

# In this exercise you'll see how simple it is to use the play() function.

# Remember: to use the play() function, you'll need simpleaudio or pyaudio installed for .wav files and ffmpeg for other kinds of files.

# Instructions
# Import play from the pydub.playback module.
# Import AudioSegment and play
from pydub import AudioSegment
from pydub.playback import play

# Create an AudioSegment instance
wav_file = AudioSegment.from_file(file="wav_file.wav", 
                                  format="wav")

# Play the audio file
play(wav_file)
# Call play() whilst passing it the wav_file AudioSegment.
