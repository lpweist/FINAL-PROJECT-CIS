import ephem
from datetime import datetime


def getcoords(iss_single):
  #break into 3 lines to turn into TLE format
  line1 = iss_single["header"]
  line2 = iss_single["line1"]
  line3 = iss_single["line2"]

  iss = ephem.readtle(line1, line2, line3)
  you = ephem.Observer()
  you.date = datetime.now()
  iss.compute(you)
  print('%s %s' % (iss.sublat, iss.sublong))
  return iss
