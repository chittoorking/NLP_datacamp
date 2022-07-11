# Acme are very impressed with your work so far. So they've sent over two more folders of audio files.

# One folder is called pre_purchase and contains audio snippets from customers who are pre-purchase, like pre_purchase_audio_25.mp3.

# And the other is called post_purchase and contains audio snippets from customers who have made a purchase (post-purchase), like post_purchase_audio_27.mp3.

# Upon inspecting the files you find there's about 50 in each and they're in the .mp3 format.

# Acme want to know if you can build a classifier to classify future calls. You tell them you sure can.

# So in this exercise, you'll go through each folder and convert the audio files to .wav format using convert_to_wav() so you can transcribe them.

# Convert the files in pre_purchase to .wav using convert_to_wav().
# Convert the files in post_purchase to .wav using convert_to_wav().

# Convert post purchase
for file in post_purchase:
    print(f"Converting {file} to .wav...")
    convert_to_wav(file)

# Convert pre purchase
for file in pre_purchase:
    print(f"Converting {file} to .wav...")
    convert_to_wav(file)
