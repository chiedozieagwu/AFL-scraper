import requests
import json
import pandas as pd

url = "https://api.afl.com.au/statspro/playersStats/seasons/CD_S2022014?playerNameLike=&playerPosition=&teamId="

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://www.afl.com.au/',
  'x-media-mis-token': '10555e48964a615dec37e015bb6a126a',
  'Origin': 'https://www.afl.com.au',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'Connection': 'keep-alive',
  'Cookie': 'JSESSIONID=7305BD0EBAB261737DE892730BDB48BF'
}

r = requests.get(url, headers=headers)

playerdata = r.json()

df = pd.json_normalize(playerdata['players'])

df.to_csv('playerdata.csv', index=False)
