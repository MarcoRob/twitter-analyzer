import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'Phwgk7y3GM3WoG60v9utSZEiR'
consumer_secret = '5qrMEcxXhbqjzw8ZeDCAZMwMGlqXCKqGE3eCBvCHMBleUagvO2'
access_token = '384061672-fJUvP0ldbgsI8BRCrseFuh95K9kGh5zs44AB1UPR'
access_secret = 'DHW9Oz2tHDaMo3tt2YJhw6fDaBEGf6b1cdaXtKHnWjUQ6'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)

user = api.get_user('twitter')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)