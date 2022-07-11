# f you've made some changes to your audio files, or if they've got the wrong file extension, you can use PyDub to export and save them as new audio files.

# You can do this by using the .export() function on any instance of an AudioSegment you've created. The export() function takes two parameters, out_f, or the destination file path of your audio file and format, the format you'd like your new audio file to be. Both of these are strings. format is "mp3" by default so be sure to change it if you need.

# In this exercise, you'll import this .mp3 file (mp3_file.mp3) and then export it with the .wav extension using .export().

# Remember, to work with files other than .wav, you'll need ffmpeg.

# Import mp3_file.mp3 and save it to mp3_file.
# Export mp3_file with the file name mp3_file.wav with "wav" format.

from pydub import AudioSegment

# Import the .mp3 file
mp3_file = AudioSegment.from_file('mp3_file.mp3')

# Export the .mp3 file as wav
mp3_file.export(out_f='mp3_file.wav',
                format='wav')
