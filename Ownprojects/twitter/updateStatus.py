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

api = tweepy.API(auth)

me = api.me()
print(me.screen_name)

img_obj = api.media_upload("barney.png")
new_status = api.update_status("gooodddd morning vietnam", media_ids=[img_obj.media_id_string])
# new_status.destroy()
