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

user = api.get_user("elonmusk")
user_timeline = user.timeline()

# status_obj = api.get_status("1285196013020610562")
# try:
#     for i in range(50):
#         status_obj_id = user_timeline[i].id
#         status_obj = api.get_status(status_obj_id)
#
#         print(status_obj.text, status_obj.user.screen_name)
# except IndexError:
#     print('error')

user_timeline_status_obj = user_timeline[0]
status_obj_id = user_timeline_status_obj.id
status_obj_screen_name = user_timeline_status_obj.user.screen_name
status_obj_url = f"https://twitter.com/{status_obj_screen_name}/status/{status_obj_id}"
print(status_obj_url)

# api.retweet(status_obj_id)
# api.create_favorite(status_obj_id)
my_reply = api.update_status(status_obj_screen_name, "Hello", status_obj_id)
