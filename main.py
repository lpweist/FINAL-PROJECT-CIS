#import tkinter as tk
#from tkinter import messagebox
from readjsn import readjson
import requests
from makegui import makegui

#from lib.buildgui import build_gui

if __name__ == "__main__":
  #guires = build_gui()
  isslocdata = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=json'
  isslocjson = requests.get(isslocdata, auth=('user', 'pass'))
  isslocjson_read = isslocjson.json()
  iss_single = isslocjson_read[0]

  print(iss_single)

  qsnt_ans = makegui()
  if qsnt_ans == 1:
    readjson()
  #print(qsnt_ans)

  # window = tk.Tk()
  #greeting = tk.Label(
  #   text=
  #  "Would you like to know the location of the International Space Station?",
  #  foreground="white",  # Set the text color to white
  #  background="black")  # Set the background color to black
  #root = tk.Tk()
  #canvas1 = tk.Canvas(root, width=300, height=300)
  #canvas1.pack()

#canvas1.create_window(150, 150, window=button1)
#root.mainloop()
