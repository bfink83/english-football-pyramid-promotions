from py_compile import main
from regex import F
import tweepy
from other import keys
from league_methods.prem import prem
from league_methods.championship import championship
from league_methods.league_one import league_one
from league_methods.league_two import league_two
from league_methods.national_league import national_league
from league_methods.level_6 import level_6
from league_methods.level_7 import level_7
from league_methods.level_8 import level_8

def api():
  auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
  auth.set_access_token(keys.access_token, keys.access_token_secret)

  return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
  if image_path:
    api.update_status_with_media(message, image_path)
  else:
    api.update_status(message)

  print('Tweeted Successfully!')


if __name__ == '__main__':
  api = api()
  yeah = 1

  for t in prem():
    tweet(api, t[0], t[1])

  if yeah == 0:
    for t in prem():
      tweet(api, t)

    for t in championship():
      tweet(api, t)

    for t in league_one():
      tweet(api, t)
    
    for t in league_two():
      tweet(api, t)

    for t in national_league():
      tweet(api, t)

    for t in level_6():
      tweet(api, t)

    for t in level_7():
      tweet(api, t)

    for t in level_8():
      tweet(api, t)
