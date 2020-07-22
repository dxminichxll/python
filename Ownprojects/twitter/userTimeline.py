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

def extract_timeline_as_df(timeline_list):
    columns = set()
    allowed_types = [str, int]
    tweets_data = []

    for status in timeline_list:
        # print(status.user.screen_name)
        status_dict = dict(vars(status))
        keys = status_dict.keys()
        single_tweet_data = {"user": status.user.screen_name, "author": status.author.screen_name}
        for k in keys:
            try:
                v_type = type(status_dict[k])
            except:
                v_type = None
            if v_type != None:
                if v_type in allowed_types:
                    single_tweet_data[k] = status_dict[k]
                    columns.add(k)
        tweets_data.append(single_tweet_data)

    header_cols = list(columns)
    header_cols.append("user")
    header_cols.append("author")
    header_cols.append("text")


    df = pd.DataFrame(tweets_data, columns=header_cols)
    return df

# my_timeline = api.home_timeline()
# df2 = extract_timeline_as_df(my_timeline)
# print(df2)

# ================================

user = api.get_user("realDonaldTrump")
user_timeline = user.timeline()

df3 = extract_timeline_as_df(user_timeline)
print(df3)
