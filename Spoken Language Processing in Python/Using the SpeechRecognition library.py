# To save typing speech_recognition every time, we'll import it as sr.

# We'll also setup an instance of the Recognizer class to use later.

# The energy_threshold is a number between 0 and 4000 for how much the Recognizer class should listen to an audio file.

# energy_threshold will dynamically adjust whilst the recognizer class listens to audio.

# Instructions
# Import the speech_recognition library as sr.
# Setup an instance of the Recognizer class and save it to recognizer.
# Set the recognizer.energy_threshold to 300.

# Importing the speech_recognition library
import speech_recognition as sr

# Create an instance of the Recognizer class
recognizer = sr.Recognizer()

# Set the energy threshold
recognizer.energy_threshold = 300
