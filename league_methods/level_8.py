import pandas as pd
import numpy as np
import requests

def level_8():
  leagues = ['Isthmanian League North Division', 'Isthmanian League South East Division', 'Isthmanian League South Central Division', 
           'Northern Premier League One East', 'Northern Premier League One West', 'Northern Premier League One Midlands', 
           'Southern League Division One Central', 'Southern League Division One South']
  header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
  }
  league_ids = ['11/', '12/', '238/', '5/', '6/', '298/', '8/', '9/']
  url = 'https://www.nonleaguematters.co.uk/divisions/'
  regex = ['Home', 'Away', 'W', 'D', 'L', 'F', 'A', 'GD']
  newTables = []

  # i = np.arange(1,21,1)

  for lid in league_ids:
    r = requests.get(url + lid, headers=header)
    df = pd.read_html(r.text)[1]
    df.columns = df.columns.to_flat_index()
    for r in regex:
        df = df[df.columns.drop(list(df.filter(regex=r)))]
    df = df.set_axis(['Pos', 'Team', 'Pld', 'Pts'], axis=1, copy=False)
    df = df.drop(['Pos'], axis=1)
    df = df[df['Pld'].apply(lambda x: str(x).isdigit())]
    n = len(df['Team'])
    i = np.arange(1,n+1,1)
    df = df.set_index(i)
    newTables.append(df)

    tweetStrings = []

  for i, df in enumerate(newTables):
    n = len(df['Team'])
    tweet_string_pro = leagues[i] + " Promotion Battle\n\n"
    tweet_string_pro += "Automatically Promoted Club: \n"
    tweet_string_pro += df['Team'][1] + " (Champion)\n\n"
    tweet_string_pro += "Promotion Playoff Clubs: \n" + df['Team'][2] + "\n" + df['Team'][3] + "\n"
    tweet_string_pro += df['Team'][4] + "\n" + df['Team'][5]

    tweet_string_rel = leagues[i] + " Relegation Battle\n\n"
    tweet_string_rel += df['Team'][n-4] + "\n" + df['Team'][n-3] + "\n" + df['Team'][n-2] + "\n" + df['Team'][n-1]

    tweetStrings += [tweet_string_rel, tweet_string_pro]

  return tweetStrings