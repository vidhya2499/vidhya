import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "5PJ0jQh8b6MztpbsXu0tu0cZC",
    "consumer_secret"     : "VAvy9tnSi8bZi2mraZ3vhUxsjCejicwdY6tDM8bHLZV9hs41RQ",
    "access_token"        : "968403081451974656-uypjoGaQOIyr4gAMAEP0caWm7HnvPZd",
    "access_token_secret" : "z0vmgA8qwrysaPqNc4bcBiyZXmjqtCOqK4rqrzEBZBJsR"
    }

  api = get_api(cfg)
  tweet = "Hello!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
  
