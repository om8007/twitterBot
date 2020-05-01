# -*- coding: utf-8 -*-
"""
Created on Fri May 1 2020

@author: om8007
"""
import tweepy

CONSUMER_KEY = '<paste your key>'
CONSUMER_SECRET = '<paste your key>'

ACCESS_TOKEN = '<paste your token>'
ACCESS_TOKEN_SECRET = '<paste your token>'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Verify authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create a tweet
api.update_status("Hello Twitter! I am just another bot on Twitter. \n #my_first_tweet")
