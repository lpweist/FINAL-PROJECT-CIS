import json
import requests


def readjson():
  isslocdata = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=json'
  isslocjson = requests.get(isslocdata, auth=('user', 'pass'))
  isslocjson_read = isslocjson.json()
  iss_single = isslocjson_read[0]
