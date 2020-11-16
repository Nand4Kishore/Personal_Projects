# Amazon-Fine-Food-Reviews-Analysis

### About the Dataset: 

https://www.kaggle.com/snap/amazon-fine-food-reviews

This dataset consists of reviews of fine foods from amazon. The data span a period of more than 10 years, including all ~500,000 reviews up to October 2012. Reviews include product and user information, ratings, and a plain text review. It also includes reviews from all other Amazon categories.

### Objective: 

To determine whether a review is positive or negative and build a machine learning model around it .

### Tasks Performed:

1) First the data is cleaned and pre-processed using standard NLP techniques. I have used tokenization,stemming ,stop-words removal . 

2) Then I have performed sentiment analysis on the dataset using following approach:

      1)I used the traditional Bag-of-Words (BOW) approach using Count Vectorizer in scikit.
  
      2)Then i used K nearest neighbours algorithm to perform the sentiment analysis.
