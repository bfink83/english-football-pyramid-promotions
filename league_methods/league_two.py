import pandas as pd
import numpy as np
import requests

def league_two():
  url = 'https://www.skysports.com/league-2-table'
  header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
  }
  r = requests.get(url, headers=header)

  df = pd.read_html(r.text)[0]
  df = df[['Team', 'Pts']]

  i = np.arange(1,25,1)
  df = df.set_index(i)

  tweet_string_pro = "EFL League Two Promotion Battle\n\n"
  tweet_string_pro += "Automatically Promoted Clubs: \n"
  tweet_string_pro += df['Team'][1] + " (Champion)\n"
  tweet_string_pro += df['Team'][2] + "\n\n" + df['Team'][3] + "\n"
  tweet_string_pro += "Promotion Playoff Clubs: \n" + df['Team'][4] + "\n" + df['Team'][5] + "\n" + df['Team'][6]  + "\n" + df['Team'][7]

  tweet_string_rel = "EFL League Two Relegation Battle\n\n"
  tweet_string_rel += df['Team'][23] + "\n" + df['Team'][24]

  return [tweet_string_rel, tweet_string_pro]