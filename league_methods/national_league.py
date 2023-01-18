import pandas as pd
import numpy as np
import requests

def national_league():

  url = 'https://www.nonleaguematters.co.uk/divisions/1/'
  header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
  }
  regex = ['Home', 'Away', 'W', 'D', 'L', 'F', 'A', 'GD']
  r = requests.get(url, headers=header)

  df = pd.read_html(r.text)[1]
  df.columns = df.columns.to_flat_index()
  for r in regex:
      df = df[df.columns.drop(list(df.filter(regex=r)))]
  df = df.set_axis(['Pos', 'Team', 'Pld', 'Pts'], axis=1, copy=False)
  df = df.drop(['Pos'], axis=1)
  df = df[df['Pld'].apply(lambda x: str(x).isdigit())]

  i = np.arange(1,25,1)
  df = df.set_index(i)

  tweet_string_pro = "Vanarama National League Promotion Battle\n\n"
  tweet_string_pro += "Automatically Promoted Club: \n"
  tweet_string_pro += df['Team'][1] + " (Champion)\n\n"
  tweet_string_pro += "Promotion Playoff Clubs: \n" + df['Team'][2] + "\n" + df['Team'][3] + "\n"
  tweet_string_pro += df['Team'][4] + "\n" + df['Team'][5] + "\n" + df['Team'][6]  + "\n" + df['Team'][7]

  tweet_string_rel = "Vanarama National League Relegation Battle\n\n"
  tweet_string_rel += df['Team'][21] + "\n" + df['Team'][22] + "\n" + df['Team'][23] + "\n" + df['Team'][24]

  return [tweet_string_rel, tweet_string_pro]