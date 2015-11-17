import oauth2
from keys import key, secret
import IPython
import ipdb

consumer_key = key
consumer_secret = secret
'''
def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    ipdb.set_trace()
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    #IPython.embed()
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content
'''

#home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', '', '' )

from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key, consumer_secret, "", "", auth_type='oAuth2')
r = api.request('search/tweets', {'q':'%23lootcrate', 'count':'100'})
a = list(r)

IPython.embed()