from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

#app = Flask(__name__)


# Load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)
labels = ['Negative', 'Neutral', 'Positive']

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

def classify_sentiment(tweet):
    tweet_proc = preprocess(tweet)
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')

    output = model(**encoded_tweet)

    scores = output.logits[0].detach().numpy()
    scores = softmax(scores)
    results = dict(zip(labels, scores))
    
    sentiment = labels[scores.argmax()]
    confidence = scores.max()
    
    return sentiment, confidence

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    confidence = None
    tweet = None
    
    if request.method == 'POST':
        tweet = request.form['tweet']
        sentiment, confidence = classify_sentiment(tweet)
    
    return render_template('index.html', sentiment=sentiment, confidence=confidence, tweet=tweet)

if __name__ == '__main__':
    app.run(debug=True)
