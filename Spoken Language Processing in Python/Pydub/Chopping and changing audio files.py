# Some of your audio files may have sections of redundancy. For example, you might find at the beginning of each file, there's a few seconds of static.

# Instead of wasting compute trying to transcribe static, you can remove it.

# Since an AudioSegment is iterable, and measured in milliseconds, you can use slicing to alter the length.

# To get the first 3-seconds of wav_file, you'd use wav_file[:3000].

# You can also add two AudioSegment's together using the addition operator. This is helpful if you need to combine several audio files.

# To practice both of these, we're going to remove the first four seconds of part1.wav, and add the remainder to part2.wav. Leaving the end result sounding like part_3.wav.

# Import part_1.wav and part_2.wav and save them to part_1 and part_2 respectively.
# Remove the first 4-seconds of part_1 using slicing and save the new audio to part_1_removed.
# Add part_1_removed to part_2 and save it to part_3.

from pydub import AudioSegment

# Import part 1 and part 2 audio files
part_1 = AudioSegment.from_file('part_1.wav')
part_2 = AudioSegment.from_file('part_2.wav')

# Remove the first four seconds of part 1
part_1_removed = part_1[4000:]

# Add the remainder of part 1 and part 2 together
part_3 = part_1_removed + part_2
