from functions.readjsn import readjson
from functions.makegui import makegui
from functions.do_orbital_math import getcoords

if __name__ == "__main__":
  qsnt_ans = makegui()
  if qsnt_ans == 1:
    iss_single = readjson()
    iss_decoded = getcoords(iss_single)
  print(iss_single)
