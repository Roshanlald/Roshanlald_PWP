import tweepy
 
def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
 
    auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
    auth.set_access_token(access_token,       access_token_secret)
 
    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['auth'] = auth
    return  api
 
 
 
def post_tweets():
 
    consumer_key	   =   '97cI0V11vIGKvkKIg5GhxHeVP'
    consumer_secret	   =   '8xDFl4y7wvWGldoebnJajK0bqCbE022kdHnEQ1JrJ2HQPOtVkG'
    access_token	   =   '4267985600-2NP6zuyUO9yqP5Pme4U9mJMtUzKLbsr4IwlVekC'
    access_token_secret=   'TOkpnQBguwLLtRQukCSaM5F4WitUuuldOpH8eQV3KSJ78'
 
    message = "Hello,\nHow are you doing today"
 
    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret )
 
    ret = api.update_status(status=message)
 
 
if __name__ == '__main__':
    post_tweets()
