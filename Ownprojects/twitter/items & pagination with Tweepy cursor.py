import tweepy
import webbrowser
import time
import pandas as pd

consumer_key = "lCuFbLfxWPsjEcDlpC9TCEh02"
consumer_secret = "0ljcIhBYxzLqXeuSGaq4xfvUnN0fr2s9xqzNoewyXaHRr3MSkl"

callback_uri = 'oob'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
redirect_uri = auth.get_authorization_url()
webbrowser.open(redirect_uri)

user_pin_input = input("Pin:")
auth.get_access_token(user_pin_input)

api = tweepy.API(auth, wait_on_rate_limit=True)

me = api.me()
print(me.screen_name)

# ============== itterate through tweets on timeline ==============

# for i, status in enumerate(tweepy.Cursor(api.home_timeline).items(50)):
#     print(i, status.text)

# ============== itterate through tweets from elon ==============
other_user = "elonmusk"
for i, status in enumerate(tweepy.Cursor(api.user_timeline, screen_name=other_user).items(20)):
    print(i, status.text)

# ============== itterate through friends ==============
# other_user = "elonmusk"
# elons_friends = []
# for i, _id in enumerate(tweepy.Cursor(api.friends_ids, screen_name=other_user).items(30)):
#     print(i, _id)
#     elons_friends.append(_id)
#
# api.get_user(elons_friends[0]).screen_name

# ============== search ==============
# query = "#spacex"
# for i, status in enumerate(tweepy.Cursor(api.search, q=query).items(50)):
#     print(i, status.text, status.author.screen_name)

# ============== search users==============
# query = "spacex"
# for i, user in enumerate(tweepy.Cursor(api.search_users, q=query).items(50)):
#     print(i, user.screen_name)

# ============== search users using pages==============
# def process_page(page_results):
#     for i, user in enumerate(page_results):
#         print(i, user.screen_name)
#
# query = "spacex"
# for i, page in enumerate(tweepy.Cursor(api.search_users, q=query, per_page=10).pages(10)):
#     print("page", i)
#     process_page(page)
#     print()
