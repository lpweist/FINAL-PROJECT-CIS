import tkinter as tk
from tkinter import messagebox


def makegui():
  msg_box = tk.messagebox.askquestion(
      'ISS Info',
      'Would you like to know the location of the International Space Station?',
      icon='warning')
  if msg_box == 'yes':
    return 1
  else:
    tk.messagebox.showinfo('Return', 'You will not learn where the ISS is.')
