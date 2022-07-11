# In this exercise, you'll calculate the sentiment on the customer channel of call_2.wav.

# You've split the customer channel and saved it to call_2_channel_2.wav.

# But from your experience with sentiment analysis, you know it can change sentence to sentence.

# To calculate it sentence to sentence, you split the split using NLTK's sent_tokenize() module.

# But transcribe_audio() doesn't return sentences. To try sentiment anaylsis with sentences, you've tried a paid API service to get call_2_channel_2_paid_api_text which has sentences.

# Instructions 
# Transcribe the audio of call_2_channel_2.wav and find the sentiment scores.

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create SentimentIntensityAnalyzer instance
sid = SentimentIntensityAnalyzer()

# Transcribe customer channel of call 2
call_2_channel_2_text = transcribe_audio('call_2_channel_2.wav')

# Display text and sentiment polarity scores
print(call_2_channel_2_text)
print(sid.polarity_scores(call_2_channel_2_text))

# Split call_2_channel_2_text into sentences and find the sentiment score of each sentence.

# Import sent_tokenize from nltk
from nltk import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create SentimentIntensityAnalyzer instance
sid = SentimentIntensityAnalyzer()

# Split call 2 channel 2 into sentences and score each
for sentence in sent_tokenize(call_2_channel_2_text):
    print(sentence)
    print(sid.polarity_scores(sentence))
    
# Split call_2_channel_2_paid_api_text into sentences and score the sentiment of each.

# Import sent_tokenize from nltk
from nltk import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create SentimentIntensityAnalyzer instance
sid = SentimentIntensityAnalyzer()

# Split channel 2 paid text into sentences and score each
for sentence in sent_tokenize('call_2_channel_2_paid_api_text'):
    print(sentence)
    print(sid.polarity_scores(sentence))
