from tkinter import * 

class UICheckButton(Button):
    def __init__(self, parent):
        super().__init__(parent, text='□')

    def select(self):
        self['text'] = '✓'
        
