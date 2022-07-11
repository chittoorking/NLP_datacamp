# In this exercise, we'll transcribe the audio files we converted to .wav format to text using transcribe_audio().

# Since there's lots of them and there could be more, we'll build a function create_test_list() which takes a list of filenames of audio files as input and goes through each file transcribing the text.

# create_test_list() uses our transcribe_audio() function we created earlier and returns a list of strings containing the transcribed text from each audio file.

# pre_purchase_wav_files and post_purchase_wav_files are lists of audio snippet filenames.

# Instructions 
# Use transcribe_audio() to transcribe the current file to text and add it to the text list.
# Return the text list.
def create_text_list(folder):
  # Create empty list
  text_list = []
  
  # Go through each file
  for file in folder:
    # Make sure the file is .wav
    if file.endswith(".wav"):
      print(f"Transcribing file: {file}...")
      
      # Transcribe audio and append text to list
      text_list.append(transcribe_audio(file))   
  return text_list

create_text_list(folder)

# Use create_text_list() to transcribe all post and pre purchase audio snippets.
# Check the first transcription of the post purchase text list.

# Transcribe post and pre purchase text
post_purchase_text = create_text_list(post_purchase_wav_files)
pre_purchase_text = create_text_list(pre_purchase_wav_files)

# Inspect the first transcription of post purchase
print(post_purchase_text[0])
