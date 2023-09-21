from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
# preprocess tweet as function
def preprocess(tweet):
    tweet_words = []

    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)

    tweet_proc = " ".join(tweet_words)
    return tweet_proc
# load model and tokenizer
#roberta = "cardiffnlp/twitter-roberta-base-sentiment" this is the base model
roberta = "sudhanvasp/Sentiment-Analysis" #this is the custom model that utilizes the base model with additional parameters to improve accuracy and performance
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']
#output as a function
def sentiment(encoded_tweet):
        tweet_proc = preprocess(tweet)
        encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')

        output = model(**encoded_tweet)

        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        #storing labels and scores in a dictionary in one line
        results = dict(zip(labels, scores))
         #print max score and label of the tweet
        print("Tweet: ", tweet)
        print("Sentiment: ", labels[scores.argmax()], scores.max())
        print("\n\n")
        print("In detail: ")
        return results
#input tweet
for i in range(0,5):
    tweet = input("Enter a tweet: ")
    tweet_proc = preprocess(tweet)
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    sentiment(encoded_tweet)
   