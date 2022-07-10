# Sometimes you may not want the entire audio file you're working with. The duration and offset parameters of the record() method can help with this.

# After exploring your dataset, you find there's one file, imported as nothing_at_end which has 30-seconds of silence at the end and a support call file, imported as out_of_warranty has 3-seconds of static at the front.

# Setting duration and offset means the record() method will record up to duration audio starting at offset. They're both measured in seconds.

# Instructions 1/
# Let's get the first 10-seconds of nothing_at_end_audio. To do this, you can set duration to 10.

# Convert AudioFile to AudioData
with nothing_at_end as source:
    nothing_at_end_audio = recognizer.record(source,
                                             duration=10.0,
                                             offset=None)

# Transcribe AudioData to text
text = recognizer.recognize_google(nothing_at_end_audio,
                                   language="en-US")

print(text)

# Let's remove the first 3-seconds of static of static_at_start by setting offset to 3.

# Convert AudioFile to AudioData
with static_at_start as source:
    static_art_start_audio = recognizer.record(source,
                                               duration=None,
                                               offset=3)

# Transcribe AudioData to text
text = recognizer.recognize_google(static_art_start_audio,
                                   language="en-US")

print(text)
