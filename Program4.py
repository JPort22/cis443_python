# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:44:01 2021

@author: Jimi Porter
"""
import numpy as np #import numpy for arrays and methods
import pandas as pd #importing pandas for dataframe usage
from textblob import TextBlob #importing textblob for sentiment analysis
from tabulate import tabulate
#from textblob.sentiments import NaiveBayesAnalyzer #using NaiveBayesAnalyzer for sentiment analysis instead

four = 4 #the number 4 for rating comparison
three = 3 #the number 3 for rating comparison
two = 2 #the number 2 for rating comparison

pol_neg = -.05 #low threshold for polarity classification
pol_pos = .05 #upper threshold for polarity classification

trip = pd.read_csv(r'C:\Users\Jimi Porter\Desktop\Fall 2021\CIS 443\tripadvisor_hotel_reviews.csv', encoding='utf8') #variable assigned to read data file of reviews
trip_df = pd.DataFrame(trip, columns=['Review', 'Rating']) #dataframe being made to make table of csv file

conditions = [ #this is a conditional array that aligns the star ratings for later use with their corresponding sentiment
    (trip_df['Rating'] <= two),# if the rating is less than or equal to 2
    (trip_df['Rating'] == three), #if the rating is equal to 3
    (trip_df['Rating'] >= four), #if the rating is greater than or equal to 4
    ]
values = ['Negative', 'Neutral', 'Positive'] #text sentiment to match value of rating

trip_df['StarSentiment'] = np.select(conditions, values) #sentiment column being made to give sentiment value next to star rating
trip_df.head() #view of first part of dataframe

trip_df['ReviewSentiment'] = trip_df['Review'].apply(lambda review: TextBlob(review).sentiment.polarity) #this statement makes the new column review sentiment and labels the polarity of the review
#within each row - this condition applies to each row

polarity_conditions = [ #this is a conditional array that aligns the review sentiments for later use with their corresponding sentiment text
    (trip_df['ReviewSentiment'] < pol_neg),# if the reviews polarity is less than -.05
    ((pol_neg <= trip_df['ReviewSentiment']) & (trip_df['ReviewSentiment'] <= pol_pos)), #if the reviews polarity is in between -.05 and .05
    (trip_df['ReviewSentiment'] > pol_pos), #if the reviews polarity is greater than .05
    ]
polarity_values = ['Negative', 'Neutral', 'Positive'] #text sentiment to match value of reviews polarity

trip_df['PolarityClassified'] = np.select(polarity_conditions, polarity_values)#creation of new column polarity classified or specified in words of review

trip_df['SentimentMatch'] = trip_df.StarSentiment == trip_df.PolarityClassified
#matching sentiments returns true if matched and false if not

#***Naive Bayes Sentiment Analyzer** - MY ATTEMPT AT THE EXTRA CREDIT
#for row in trip_df:
    #for review in trip_df.Review:
        #text = review
#blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
#blob_s = blob.sentiment
#blob.sentiment
#for review in blob.sentences:
    #trip_df['NB-Sentiment'] = review.sentiment
#naive_bayer_sentiment = TextBlob(trip_df['Review'], analyzer=NaiveBayesAnalyzer())
#trip_df['NaiveBayes'] = trip_df['Review'].apply(lambda review: TextBlob(review, analyzer=NaiveBayesAnalyzer()))
#for review in trip_df.NaiveBayes:
    #trip_df['NB-Sentiment'] = review.sentiment
#trip_df['NaiveBayesSentiment'] = trip_df['NaiveBayes'].sentiment

hun = 100 #hundred for percentages
#printing overall summary report
true_df = trip_df[trip_df['SentimentMatch'] == True] #makes dataframe of all matching star-text sentiments
false_len = len(trip_df) - len(true_df) # false length variable to find amount and percentage of non matching sentiments

true_per = len(true_df) / len(trip_df) * hun #percentage of true sentiments or matching
false_per = false_len / len(trip_df) * hun #percentage of false sentiments or non matching

#The following comments remain the same for all star sentiments as the format is the same as well as naming conventions
#five star sentiment report
five_star_df = trip_df[trip_df['Rating'] == 5]#making data frame of just 5 star ratings
true_five_df = five_star_df[five_star_df['SentimentMatch'] == True]#making a dataframe that just shows the amount of true sentiment 5 star ratings
five_false_len = len(five_star_df) - len(true_five_df)#gives the difference of true five star ratings and the total amount - so the false sentiments

five_true_per = len(true_five_df) / len(five_star_df) * hun#gives percentage of true sentiment five star ratings
five_false_per = five_false_len / len(five_star_df) * hun#gives percentage of false sentiment five star ratings

#four star sentiment report
four_star_df = trip_df[trip_df['Rating'] == 4]
true_four_df = four_star_df[four_star_df['SentimentMatch'] == True]
four_false_len = len(four_star_df) - len(true_four_df)

four_true_per = len(true_four_df) / len(four_star_df) * hun
four_false_per = four_false_len / len(four_star_df) * hun

#three star sentiment report
three_star_df = trip_df[trip_df['Rating'] == 3]
true_three_df = three_star_df[three_star_df['SentimentMatch'] == True]
three_false_len = len(three_star_df) - len(true_three_df)

three_true_per = len(true_three_df) / len(three_star_df) * hun
three_false_per = three_false_len / len(three_star_df) * hun

#two star sentiment report
two_star_df = trip_df[trip_df['Rating'] == 2]
true_two_df = two_star_df[two_star_df['SentimentMatch'] == True]
two_false_len = len(two_star_df) - len(true_two_df)

two_true_per = len(true_two_df) / len(two_star_df) * hun
two_false_per = two_false_len / len(two_star_df) * hun

#one star sentiment report
one_star_df = trip_df[trip_df['Rating'] == 1]
true_one_df = one_star_df[one_star_df['SentimentMatch'] == True]
one_false_len = len(one_star_df) - len(true_one_df)

one_true_per = len(true_one_df) / len(one_star_df) * hun
one_false_per = one_false_len / len(one_star_df) * hun

print('Overall Star-Sentiment Report')
print('-----------------------------')
print(f'Total # of Reviews: {len(trip_df)}')
print(f'Total # of Matching Reviews: {len(true_df)} out of {len(trip_df)}; Percent: {true_per:.1f}%')
print(f'Total # of Non-Matching Reviews: {false_len} out of {len(trip_df)}; Percent: {false_per:.1f}%')

report_list =[[5, len(five_star_df), len(true_five_df), five_true_per, five_false_len, five_false_per], 
              [4, len(four_star_df), len(true_four_df), four_true_per, four_false_len, four_false_per],
              [3, len(three_star_df), len(true_three_df), three_true_per, three_false_len, three_false_per],
              [2, len(two_star_df), len(true_two_df), two_true_per, two_false_len, two_false_per],
              [1, len(one_star_df), len(true_one_df), one_true_per, one_false_len, one_false_per]]


print(tabulate(report_list, headers=["Star(s) Given", "Total Reviews", "Matching Reviews", "% of Matching Reviews", "Non-Matching Reviews", "% of Non-Matching Reviews"]))
