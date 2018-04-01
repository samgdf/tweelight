import twitter
import time
from datetime import datetime

# Use Twitter as example remote application
twitter = oauth.remote_app('twitter',
    # unless absolute urls are used to make requests, this will be added
    # before all URLs.  This is also true for request_token_url and others.
    base_url='https://api.twitter.com/1/',
    # where flask should look for new request tokens
    request_token_url='https://api.twitter.com/oauth/request_token',
    # where flask should exchange the token with the remote application
    access_token_url='https://api.twitter.com/oauth/access_token',
    # twitter knows two authorizatiom URLs.  /authorize and /authenticate.
    # they mostly work the same, but for sign on /authenticate is
    # expected because this will give the user a slightly different
    # user interface on the twitter side.
    authorize_url='https://api.twitter.com/oauth/authenticate',
    # the consumer keys from the twitter application registry.
    consumer_key='',
    consumer_secret=''
)

api = twitter.Api(consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret='')

userSpecified = england

statuses = api.GetUser(screen_name=tweetTable)
api.CreateFriendship(screen_name=userSpecified, follow=True)
api.UpdateFriendship(screen_name=userSpecified, follow=False)
api.DestroyFriendship(screen_name=userSpecified)
