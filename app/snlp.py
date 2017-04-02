from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()

def sentiment(text):
  return sentiment_analyzer.polarity_scores(text)
