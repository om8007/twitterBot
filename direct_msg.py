# -*- coding: utf-8 -*-
"""
Created on Wed 20 May 2020

@author: om8007
"""

#explorer
import tweepy
import logging

CONSUMER_KEY = '<paste your key>'
CONSUMER_SECRET = '<paste your key>'

ACCESS_TOKEN = '<paste your token>'
ACCESS_TOKEN_SECRET = '<paste your token>'

# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# get user (to)
user = api.get_user(screen_name='om_8007')
# send direct msg
logger.info(f"Sending msg to {user.screen_name}")
# api.send_direct_message(user.id, "Hi, I am learning to send direct msg with Tweepy.")

# send msg with quick reply options
reply_options = [
            {
              "label": "Red",
            },
            {
              "label": "Blue",
            },
            {
              "label": "Black",
            },
            {
              "label": "Pink",
              },
            {
              "label": "Green",
            },
            {
              "label": "White",
            }]

logger.info(f"Sending msg with quick reply options to {user.screen_name}")
api.send_direct_message(user.id, "What's your favorite color?"
 , quick_reply_type='options'
 ,quick_reply_options = reply_options
 )

 # P.S. Messages with quick reply options may not work for everyone. I have tweaked the api.py code in tweepy package to get the job done. 