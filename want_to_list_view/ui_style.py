
from tkinter import ttk, font

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

        style.configure('field.TLabel', background='pink')
        style.configure('field.TLabel', font=('Centry Gothic', 15, 'bold'))

        style.configure('subfield.TLabel', background='misty rose')
        style.configure('subfield.TLabel', font=('Centry Gothic', 15, 'bold'))

        style.configure('yellow_alt_1.TLabel', background='#FFEC8B')  # light grey
        style.configure('yellow_alt_2.TLabel', background='#FCDC3B')  # dark grey

        style.configure('grey_alt_1.TLabel', background='#F2F2F2')  # light yellow 
        style.configure('grey_alt_2.TLabel', background='#DCDCDC')  # dark yellow

        return style