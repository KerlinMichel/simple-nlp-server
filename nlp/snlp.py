from nltk.corpus import cmudict
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize

sentiment_analyzer = SentimentIntensityAnalyzer()
pron_dict = cmudict.dict()

def num_syl(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in pron_dict[word.lower()]][0]

def num_sent(text):
  return len(sent_tokenize(text))

def sentiment(text):
  return sentiment_analyzer.polarity_scores(text)

def flesch_kincaid_grade_level(text):
  words = word_tokenize(text.lower())
  num_words = float(len(words))
  num_syll = 0
  for word in words:
    if word in pron_dict:
      num_syll += num_syl(word)
  num_sents = float(num_sent(text))
  num_syll = float(num_syll)
  return (0.39*(num_words/num_sents)) + (11.8*(num_syll/num_words)) - 15.59
