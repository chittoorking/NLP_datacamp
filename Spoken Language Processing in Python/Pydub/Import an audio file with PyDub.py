# PyDub's AudioSegment class makes it easy to import and manipulate audio files with Python.

# In this exercise, we'll import an audio file of interest by creating an instance of AudioSegment.

# To import an audio file, you can use the from_file() function on AudioSegment and pass it your target audio file's pathname as a string. The format parameter gives you an option to specify the format of your audio file, however, this is optional as PyDub will automatically infer it.

# PyDub works with .wav files without any extra dependencies but for other file types like .mp3, you'll need to install ffmpeg.

# A sample audio file has been setup as wav_file.wav, you can listen to it here.

# Instructions
# Import AudioSegment from pydub.
# Call the from_file method and pass it the audio file pathname.

# Import AudioSegment from Pydub
from pydub import AudioSegment

# Create an AudioSegment instance
wav_file = AudioSegment.from_file(file='wav_file.wav', 
                                  format="wav")

# Check the type
print(type(wav_file))
