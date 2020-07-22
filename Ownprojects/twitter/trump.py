import tweepy
import webbrowser
import time
import pandas as pd

consumer_key = "lCuFbLfxWPsjEcDlpC9TCEh02"
consumer_secret = "0ljcIhBYxzLqXeuSGaq4xfvUnN0fr2s9xqzNoewyXaHRr3MSkl"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
redirect_uri = auth.get_authorization_url()
webbrowser.open(redirect_uri)

user_pin_input = input("Pin:")
auth.get_access_token(user_pin_input)

api = tweepy.API(auth, wait_on_rate_limit=True)

me = api.me()
print(me.screen_name)

# def process_page(page_results):
#     for i, status in enumerate(page_results):
#         # if "RT" not in status.text:
#         #     if "black" in status.text:
#         print(i, status.text, status.id)

other_user = "realDonaldTrump"
for i, status in enumerate(tweepy.Cursor(api.user_timeline, screen_name=other_user).items(1000)):
    # if "RT" not in status.text:
    #     if "black" in status.text:
    print(i, status.text, status.id)
