# If you're trying to transcribe phone calls, there's a chance they've been recorded in stereo format, with one speaker on each channel.

# As you've seen, it's hard to transcribe an audio file with more than one speaker. One solution is to split the audio file with multiple speakers into single files with individual speakers.

# PyDub's split_to_mono() function can help with this. When called on an AudioSegment recorded in stereo, it returns a list of two separate AudioSegment's in mono format, one for each channel.

# In this exercise, you'll practice this by splitting this stereo phone call (stereo_phone_call.wav) recording into channel 1 and channel 2. This separates the two speakers, allowing for easier transcription.

# Instructions
# Import AudioSegment from pydub.
# Create an AudioSegment instance stereo_phone_call with stereo_phone_call.wav.
# Split stereo_phone_call into channels using split_to_mono() and check the channels of the resulting output.
# Save each channel to new variables, phone_call_channel_1 and phone_call_channel_2.

# Import AudioSegment
from pydub import AudioSegment

# Import stereo audio file and check channels
stereo_phone_call = AudioSegment.from_file('stereo_phone_call.wav')
print(f"Stereo number channels: {stereo_phone_call.channels}")

# Split stereo phone call and check channels
channels = stereo_phone_call.split_to_mono()
print(f"Split number channels: {channels[0].channels}, {channels[1].channels}")

# Save new channels separately
phone_call_channel_1 = channels[0]
phone_call_channel_2 = channels[1]
