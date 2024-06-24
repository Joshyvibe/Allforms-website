from django.shortcuts import render

import json


try:
    # Try to open the cached tweets file
    with open('tweets_cache.json', 'r') as file:
        the_tweets = json.load(file)
    print("Loaded tweets from cache.")

except FileNotFoundError:
    # If the file is not found, handle the exception
    print("Error: tweets_cache.json not found. Please ensure the file exists.")

    # Optionally, define a default behavior or initialize an empty list
    the_tweets = []


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
   
   




