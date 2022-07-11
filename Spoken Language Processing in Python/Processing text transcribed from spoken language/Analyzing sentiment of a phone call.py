# Once you've transcribed the text from an audio file, it's possible to perform natural language processing on the text.

# In this exercise, we'll use NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) to analyze the sentiment of the transcribed text of call_2.wav.

# To transcribe the text, we'll use the transcribe_audio() function we created earlier.

# Once we have the text, we'll use NLTK's SentimentIntensityAnalyzer() class to obtain a sentiment polarity score.

# .polarity_scores(text) returns a value for pos (positive), neu (neutral), neg (negative) and compound. Compound is a mixture of the other three values. The higher it is, the more positive the text. Lower means more negative.

# Instructions
# Instantiate an instance of SentimentIntensityAnalyzer() and save it to the variable sid.
# Transcribe the target call and save it to call_2_text.
# Print the polarity_scores() of call_2_text.

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create SentimentIntensityAnalyzer instance
sid = SentimentIntensityAnalyzer()

# Let's try it on one of our phone calls
call_2_text = transcribe_audio('call_1.wav')

# Display text and sentiment polarity scores
print(call_2_text)
print(sid.polarity_scores(call_2_text))
