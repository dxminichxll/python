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
# ============= follow users ============= 
# print(user.followers_count, user.friends_count)
my_new_friends = []
user_friends = user.friends()
# print(len(user_friends))
for friend in user_friends:
    if friend.followers_count > 1000000:
        print(friend.screen_name)
        relationship = api.create_friendship(friend.screen_name)
        my_new_friends.append(friend.screen_name)
# ============= unfollow users =============
# to_remove = my_new_friends
# print(my_new_friends)
# for username in to_remove:
#     api.destroy_friendship(username)
