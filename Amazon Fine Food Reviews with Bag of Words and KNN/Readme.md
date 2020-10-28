Amazon-Fine-Food-Reviews-Analysis

About the Dataset: 
https://www.kaggle.com/snap/amazon-fine-food-reviews

This dataset consists of reviews of fine foods from amazon. The data span a period of more than 10 years, including all ~500,000 reviews up to October 2012. Reviews include product and user information, ratings, and a plain text review. It also includes reviews from all other Amazon categories.

Aim: 

To determine whether a review is positive or negative and build a machine learning model around it .


First the data is cleaned and pre-processed using standard NLP techniques like tokenization,stemming ,stop-words removal among others. Then I have performed sentiment analysis on the dataset using different approaches.

1) The first approach used is the traditional Bag-of-Words (BOW) approach using Tfidf and Count Vectorizer in scikit. In this case the word level tfidf vectorizer using the Logistic Regression gave best results for me with an accuracy of about a little more than 86%.

2) In the second approach I have used the Google Word2Vec word embeddings from Gensim librray and trained a LSTM model in Keras on them. This method also gives an accuracy of about 85%.
