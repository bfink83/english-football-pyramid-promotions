import pandas as pd
import numpy as np
import dataframe_image as dfi
import requests

# def prem():
#   url = 'https://www.skysports.com/premier-league-table'
#   header = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
#     "X-Requested-With": "XMLHttpRequest"
#   }
#   r = requests.get(url, headers=header)

#   df = pd.read_html(r.text)[0]
#   df['Rem'] = [38 - p for p in df['Pl']]
#   df = df[['Team', 'Pts', 'Rem']]

#   n = len(df['Team'])
#   i = np.arange(1, n + 1, 1)
#   df = df.set_index(i)

#   # tweet_string_ucl = "Premier League Champions League Qualifiers\n\n"
#   # tweet_string_ucl += df['Team'][1] + " (Champion)\n"
#   # tweet_string_ucl += df['Team'][2] + "\n" + df['Team'][3]
#   # tweet_string_ucl += "\n" + df['Team'][4] + "\n\n"
#   # tweet_string_ucl += df['Team'][1] + " (" + str(df['Pts'][1]) + ") (Champion)\n"
#   # tweet_string_ucl += df['Team'][2] + " (" + str(df['Pts'][2]) + ")" + "\n" + df['Team'][3] + " (" + str(df['Pts'][3]) + ")"
#   # tweet_string_ucl += "\n" + df['Team'][4] + " (" + str(df['Pts'][4]) + ")" + "\n\n"


#   tweet_string_ucl = """Premier League Champions League Qualifiers

# {0} ({1}) (Champion)
# {2} ({3})
# {4} ({5})
# {6} ({7})
#   """
#   tweet_string_ucl = tweet_string_ucl.format(df['Team'][1], df['Pts'][1], df['Team'][2], df['Pts'][2], df['Team'][3], df['Pts'][3], df['Team'][4], df['Pts'][4])

#   print(len(tweet_string_ucl))

#   # tweet_string_europa = "Premier League Europa and Conference League Qualifiers\n\n"
#   # tweet_string_europa += "Europa League: \n" + df['Team'][5]
#   # tweet_string_europa += "\n" + df['Team'][6] + "\n\n"
#   # tweet_string_europa += "Europa Conference League: \n" + df['Team'][7]

#   tweet_string_europa = """Premier League Europa and Conference League Qualifiers

# Europa League:
# {0} ({1})
# {2} ({3})

# Europa Conference League: 
# {4} ({5})
#   """

#   tweet_string_europa = tweet_string_europa.format(df['Team'][5], df['Pts'][5], 
#                                                     df['Team'][6], df['Pts'][6], 
#                                                     df['Team'][7], df['Pts'][7])

#   # tweet_string_rel = "Premier League Relegation Zone\n\n"
#   # tweet_string_rel += df['Team'][18] + "\n" 
#   # tweet_string_rel += df['Team'][19] + "\n" 
#   # tweet_string_rel += df['Team'][20]

#   tweet_string_rel = """Premier League Relegation Zone
# {0} ({1})
# {2} ({3})
# {4} ({5})
#   """

#   tweet_string_rel = tweet_string_rel.format(df['Team'][n-2], df['Pts'][n-2], df['Team'][n-1], df['Pts'][n-1], df['Team'][n], df['Pts'][n])


#   print(df['Team'].str.len().max())
#   return [tweet_string_rel, tweet_string_europa, tweet_string_ucl]
#   # dfi.export(df,"mytable.png")
#   # return ["test", "./mytable.png"]


def prem():
  url = 'https://www.skysports.com/premier-league-table'
  header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
  }
  r = requests.get(url, headers=header)

  df = pd.read_html(r.text)[0]
  df['Rem'] = [38 - p for p in df['Pl']]
  df = df[['Team', 'Pts', 'Rem']]

  n = len(df['Team'])
  i = np.arange(1, n + 1, 1)
  df = df.set_index(i)

  dfi.export(df,"temp/mytable.png")
  img1 = img2 = img3 = 'temp/mytable.png'

  cap1 = 'test1'
  cap2 = 'test2'
  cap3 = 'test3'




  return [[cap3, img3], [cap2, img2], [cap1, img1]]
  # dfi.export(df,"mytable.png")
  # return ["test", "./mytable.png"]