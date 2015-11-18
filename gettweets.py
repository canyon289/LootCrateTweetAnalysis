from keys import key, secret
import IPython
import ipdb
import pickle
import pandas as pd
import webbrowser
pd.set_option('display.width', 240)

consumer_key = key
consumer_secret = secret


from TwitterAPI import TwitterAPI, TwitterRestPager

def get_tweets():
    '''
    Get's tweets with Twitter hashtag api
    '''
    api = TwitterAPI(consumer_key, consumer_secret, '', '', auth_type='oAuth2')
    pager = TwitterRestPager(api, 'search/tweets', {'q':'%23lootcrate', 'count':100}) 

    a = []

    for i,item in enumerate(pager.get_iterator()):
        if 'text' in item:
            a.append(item)
            print(i)
        elif 'message' in item and item['code'] == 88:
            print('Rate Exceeded')
            break
    
    pickle.dump(a, open('tweets.p', 'rb'))
    return
    
def text_series(tweets):
    '''
    Gets tweets and usernames
    '''
    text_list = [[t['user']['screen_name'], t['text'], t['id'], t['created_at'], t['retweet_count']] for t in tweets]
    user_name = [tweet['user']['screen_name'] for tweet in tweets]

    return pd.DataFrame(text_list, columns = ['user_name', 'text', 'id', 'created_at', 'retweet_count'])

#Filter out tweets that contains

def open_tweet(df, index):
    '''
    Function for opening page for specific tweet
    '''
    id = df.ix[index, 'id']
    webbrowser.open('https://twitter.com/statuses/' + str(id))
    return
    
tweets = pickle.load(open('tweets.p', 'rb'))
df = text_series(tweets)
df['created_at'] = pd.to_datetime(df['created_at'])
sub_df = df[~df['text'].str.contains('Loot Crate is awesome! SAVE $3', regex = False)]
