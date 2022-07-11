You've seen how to convert a single file using PyDub but what if you had a folder with multiple different file types?

For this exercise, we've setup a folder which has .mp3, .m4a and .aac versions of the good-afternoon audio file.

We'll use PyDub to open each of the files and export them as .wav format so they're compatible with speech recognition APIs.

Instructions
Pass audio_file to the from_file() function.
Use export() to export wav_filename with the format ".wav".

# Loop through the files in the folder
for audio_file in folder:
    
	# Create the new .wav filename
    wav_filename = os.path.splitext(os.path.basename(audio_file))[0] + ".wav"
        
    # Read audio_file and export it in wav format
    AudioSegment.from_file(audio_file).export(out_f=wav_filename, 
                                      format='wav')
        
    print(f"Creating {wav_filename}...")
