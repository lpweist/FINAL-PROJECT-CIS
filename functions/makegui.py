import tkinter as tk
from tkinter import messagebox
from functions.do_orbital_math import getcoords
from functions.plotonmap import plotmap
from functions.readjsn import readjson


def makegui():
  msg_box = tk.messagebox.askquestion(
      'ISS Info',
      'Would you like to know the location of the International Space Station?',
      icon='warning')
  if msg_box == 'yes':
    iss_single = readjson()
    iss_decoded = getcoords(iss_single)
    plotmap(iss_decoded)
    tk.messagebox.showinfo(
        'Results', 'The ISS is at ' + str(iss_decoded.sublat) + ',' +
        str(iss_decoded.sublong) + '. View the map at issmap.html.')
    return 1
  else:
    tk.messagebox.showinfo('Return', 'You will not learn where the ISS is.')
