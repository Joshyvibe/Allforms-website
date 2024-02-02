from django.shortcuts import render
from ntscraper import Nitter

import json


# Check if the tweets are already saved in a file
try:
    with open('tweets_cache.json', 'r') as file:
        the_tweets = json.load(file)
    print("Loaded tweets from cache.")
except FileNotFoundError:
    # If the file is not found, scrape the tweets and save them to a file
    the_tweets = []
    scraper = Nitter()
    tweets = scraper.get_tweets('allformsltd', mode='user', number=5)
    for tweet in tweets['tweets']:
        data = [tweet['link'], tweet['text'], tweet['user']['avatar'], tweet['date']]
        the_tweets.append(data)

    # Save the tweets to a file
    with open('tweets_cache.json', 'w') as file:
        json.dump(the_tweets, file, indent=2)
    print("Scraped tweets and saved to cache.")

# Access the first tweet
#if the_tweets:
#    print("Text of the first tweet:", the_tweets[0][0])





def home(request):
    try:
        with open('tweets_cache.json', 'r') as file:
            tweets = json.load(file)
        print("Loaded tweets from cache for views.")
    except FileNotFoundError:
        # Handle the case where the file is not found (tweets not scraped yet)
        tweets = []
        print("No cached tweets found.")

    context = {'tweets': tweets}

    return render(request, 'home.html', context)
   
   




