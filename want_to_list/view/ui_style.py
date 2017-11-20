from tkinter import *
from tkinter import ttk

class UIStyle(ttk.Style):
    def __init__(self):
        super().__init__()
        self.theme_use('classic')

    def get_original():
        style = UIStyle()

        # Root
        style.configure('.', font=('Roboto', 15))
        style.configure('.', background='white')
        style.configure('.', borderwidth=0)

        # Notebook
        style.configure('TNotebook.Tab', background='#E0EEE0')  # light green
        style.map('TNotebook.Tab', background=[('selected', '#93DB70')])  # dark green
        style.configure('TNotebook.Tab', borderwidth=3)

        # Labels
        style.configure('TLabel', padding=2)

        style.configure('options.TLabel', background='#E0EEE0')  # light green

        style.configure('sort_label.TLabel', background='misty rose')
        style.configure('sort_label.TLabel', anchor=CENTER)

        style.configure('field.TLabel', background='pink')
        style.configure('field.TLabel', font=('Centry Gothic', 15, 'bold'))

        style.configure('subfield.TLabel', background='misty rose')
        style.configure('subfield.TLabel', font=('Centry Gothic', 15, 'bold'))

        style.configure('yellow_alt_1.TLabel', background='#FFEC8B')  # light yellow
        style.configure('yellow_alt_2.TLabel', background='#FCDC3B')  # dark yellow

        style.configure('grey_alt_1.TLabel', background='#F2F2F2')  # light grey 
        style.configure('grey_alt_2.TLabel', background='#DCDCDC')  # dark grey

        return style
