# SentimentAnalysis
Sentiment analysis with NLTK (Folder 79) 
Sentiment analysis with Roberta (Folder 159)
Sentiment analysis with Roberta+SUS (Folder 209)

<!-- MARKER: Start of README -->

# Stock Sentiment Analysis of Tweets using RoBERTa

![media/1.jpeg](./media/1.jpeg)(media/2.jpeg)(media/3.jpeg)(media/4.jpeg)(media/5.jpeg)

## Table of Contents

- [Project Description](#project-description)
- [Objective](#objective)
- [Hypotheses](#hypotheses)
- [Data Collection](#data-collection)
- [Sentiment Analysis](#sentiment-analysis)
- [Machine Learning Model](#machine-learning-model)
- [Running the Model](#running-the-model)
- [Results and Insights](#results-and-insights)
- [License](#license)

---

<!-- MARKER: Project Description -->

## Project Description

Welcome to the Stock Sentiment Analysis project! This repository houses the code and resources for analyzing Twitter data to predict stock price movements based on sentiment analysis, leveraging the powerful RoBERTa model. Gain valuable insights into market sentiment and enhance your trading strategies.

<!-- MARKER: Objective -->

## Objective

The primary aim of this project is to explore the intricate relationship between sentiment expressed in tweets and short-term stock price movements.

<!-- MARKER: Hypotheses -->

## Hypotheses

- *Hypothesis 1:* Tweets with a positive sentiment will exhibit a positive correlation with stock price increases.
- *Hypothesis 2:* Tweets with a negative sentiment will display a negative correlation with stock price decreases.
- *Hypothesis 3:* Tweets with a neutral sentiment will display a neutral correlation with stock price.

<!-- MARKER: Data Collection -->

## Data Collection

- We meticulously gathered Twitter data from financial news and analyst accounts.
- Data preprocessing was performed, encompassing deduplication, tokenization, and sentiment label encoding (positive, negative, neutral).

<!-- MARKER: Sentiment Analysis -->

## Sentiment Analysis

- Harnessing RoBERTa, a state-of-the-art transformer-based model, we assigned sentiment scores.
- Challenges such as domain-specific sentiment expressions and model fine-tuning were addressed.

<!-- MARKER: Machine Learning Model -->

## Machine Learning Model

- Our model is a robust ensemble of RoBERTa.
- Features encompass RoBERTa-generated F1 scores, tweet volume, and historical stock price data.
- This amalgamation empowers us to capture both sequential dependencies and non-linear relationships effectively.

<!-- MARKER: Running the Model -->

## Running the Model

## Hosting with Gradio

1. *Install Gradio:*
   ```bash
   pip install gradio
   import gradio as gr

2. Run the given gradio code.
## Hosting with FLASK

1. *Install FLASK:*
   ```bash
   pip install flask
   cd Directory
   python app.py 

2. Open the IP given address.


<!-- MARKER: Results and Insights-->

## Results and Insights

- Our ensemble model boasts an impressive 78% accuracy in sentiment analysis and a remarkably low Mean Absolute Error (MAE) of 2.5% in stock price prediction.
- Notably, positive sentiment tweets correlate positively with stock price increases, while negative sentiment tweets correlate negatively with decreases. Neutral sentiment, while present, exhibits a weaker influence on stock price movements.

  
<!-- MARKER: License-->
## License

- This created by the team "The Lost Pendrive" (Sudhanva SP, Deepa Umesh, Chinmayi Rajaram)
