You've seen how to import and manipulate a single audio file using PyDub. But what if you had a folder with multiple audio files you needed to convert?

In this exercise we'll use PyDub to format a folder of files to be ready to use with speech_recognition.

You've found your customer call files all have 3-seconds of static at the start and are quieter than they could be.

To fix this, we'll use PyDub to cut the static, increase the sound level and convert them to the .wav extension.

You can listen to an unformatted example here.

Let's start with one file. Import account_help.mp3 and cut off the first 3-seconds (3000 milliseconds) of static.



file_with_static = AudioSegment.from_file('account_help.mp3')

# Cut the first 3-seconds of static off
file_without_static = file_with_static[3000:]

# Increase the volume by 10dB
louder_file_without_static = file_without_static + 10


## Now for multiple files. Use from_file() to import each audio_file and export the louder files without static with the "wav" format

for audio_file in folder:
    file_with_static = AudioSegment.from_file(audio_file)

    # Cut the 3-seconds of static off
    file_without_static = file_with_static[3000:]

    # Increase the volume by 10dB
    louder_file_without_static = file_without_static + 10
    
    # Create the .wav filename for export
    wav_filename = os.path.splitext(os.path.basename(audio_file))[0] + ".wav"
    
    # Export the louder file without static as .wav
    louder_file_without_static.export(wav_filename, format='wav')
    print(f"Creating {wav_filename}...")
