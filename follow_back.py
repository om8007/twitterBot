# -*- coding: utf-8 -*-
"""
Created on Wed 6 May 2020

@author: om8007
"""
#explorer
import tweepy
import logging
import time

CONSUMER_KEY = '<paste your key>'
CONSUMER_SECRET = '<paste your key>'

ACCESS_TOKEN = '<paste your token>'
ACCESS_TOKEN_SECRET = '<paste your token>'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

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

# Scan every 1 min for any new follower
while True:
    follow_followers(api)
    logger.info("Waiting...")
    time.sleep(60)
