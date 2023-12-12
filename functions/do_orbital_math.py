import ephem


def getcoords(iss_single):
  #break into 3 lines to turn into TLE format
  line1 = iss_single["header"]
  line2 = iss_single["line1"]
  line3 = iss_single["line2"]

  iss = ephem.readtle(line1, line2, line3)
  iss.compute()
  print('%s %s' % (iss.sublong, iss.sublat))
  return iss
