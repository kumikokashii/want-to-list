
from tkinter import *

from .ui_tab_in_notebook import *

class UISettings(UITabInNB):
    def __init__(self, parent, tab_name):
        super().__init__(parent, tab_name)

    def refresh(self):
        self.cleanup()

        button_1 = Button(self, text='Save & Exit', 
                          command=self.controller.save_exit)
        button_2 = Button(self, text='Start Fresh',
                          command=self.controller.start_fresh)

        table = [button_1, button_2]
        for i in range(len(table)):
            table[i].grid(row=i, column=0, sticky=W+E, padx=2, pady=5)
