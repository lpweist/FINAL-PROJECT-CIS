import requests
from itertools import cycle


def readjson():
  isslocdata = 'https://api.wheretheiss.at/v1/satellites/25544/tles'
  isslocjson = requests.get(isslocdata, auth=('user', 'pass'))
  isslocjson_read = isslocjson.json()

  return isslocjson_read
