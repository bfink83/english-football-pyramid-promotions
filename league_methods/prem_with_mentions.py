import pandas as pd
import numpy as np
import requests

def prem():
  url = 'https://www.skysports.com/premier-league-table'
  header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
  }
  r = requests.get(url, headers=header)

  handles = pd.read_excel (r'club_twitter_handles.xlsx')

  df = pd.read_html(r.text)[0]
  df = df[['Team', 'Pts']]

  i = np.arange(1,21,1)
  df = df.set_index(i)

  # twitter_handles = [None]
  twitter_handles = []
  for team in df['Team']:
    twitter_handles.append(handles.loc[handles.Team == team, 'Handle'].values[0])

  df['Handles'] = twitter_handles

  tweet_string_ucl = "Premier League Champions League Qualifiers\n\n"
  tweet_string_ucl += df['Team'][1] + " (" + df['Handles'][1] + ") (Champion)\n"
  tweet_string_ucl += df['Team'][2] + " (" + df['Handles'][2] + ")" + "\n" + df['Team'][3] + " (" + df['Handles'][3] + ")"
  tweet_string_ucl += "\n" + df['Team'][4] + " (" + df['Handles'][4] + ")" + "\n\n"

  tweet_string_europa = "Premier League Europa and Conference League Qualifiers"
  tweet_string_europa += "Europa League: \n" + df['Team'][5] + " (" + df['Handles'][5] + ")" 
  tweet_string_europa += "\n" + df['Team'][6] + " (" + df['Handles'][6] + ")" + "\n\n"
  tweet_string_europa += "Europa Conference League: \n" + df['Team'][7] + " (" + df['Handles'][7] + ")"

  tweet_string_rel = "Premier League Relegation Zone\n\n"
  tweet_string_rel += df['Team'][18] + " (" + df['Handles'][18] + ")" + "\n" 
  tweet_string_rel += df['Team'][19] + " (" + df['Handles'][19] + ")" + "\n" 
  tweet_string_rel += df['Team'][20] + " (" + df['Handles'][20] + ")"

  return [tweet_string_rel, tweet_string_europa, tweet_string_ucl]