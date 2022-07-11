# Speech recognition works best on clean, audible speech. If your audio files are too quiet or too loud, it can hinder transcription.

# In this exercise, you'll see how to make an AudioSegment quieter or louder.

# Since the play() function won't play your changes in the DataCamp classroom.

# The baseline audio file, volume_adjusted.wav can be heard here.

# Instructions
# Import volume_adjusted.wav and lower its volume by 60 dB and save it to a new variable quiet_volume_adjusted.

# Import the target audio file, increase its volume by 15 dB and save it to the variable louder_volume_adjusted.

from pydub import AudioSegment

# Import audio file
volume_adjusted = AudioSegment.from_file('volume_adjusted.wav')

# Lower the volume by 60 dB
quiet_volume_adjusted = volume_adjusted - 60


from pydub import AudioSegment

# Import audio file
volume_adjusted = AudioSegment.from_file('volume_adjusted.wav')

# Increase the volume by 15 dB
louder_volume_adjusted = volume_adjusted + 15
