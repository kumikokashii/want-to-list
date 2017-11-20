
from tkinter import *

from .ui_tab_in_notebook import *
from ..model.organizer import *

class UISettings(UITabInNB):
    def __init__(self, parent, tab_name):
        super().__init__(parent, tab_name)

    def refresh(self):
        self.cleanup()

        button_1 = Button(self, text='Save & Exit', 
                          command=self.controller.save_exit)
        button_2 = Button(self, text='Start Fresh',
                          command=self.controller.start_fresh)
        button_3 = Button(self, text='Load',
                          command=self.load_onclick)
        button_4 = Button(self, text='Save As',
                          command=self.save_as_onclick)

        table = [button_1, button_2, button_3, button_4]
        for i in range(len(table)):
            table[i].grid(row=i, column=0, sticky=W+E, padx=2, pady=5)

    def load_onclick(self):
        file_path = filedialog.askopenfilename(
                        initialdir = Organizer.app_dir,
                        title = 'Select a file!',
                        filetypes = (('Want To List files', '*.wtl'), ('all files', '*.*')))

        if file_path != '':  # File is selected
            self.controller.load(file_path)

    def save_as_onclick(self):
        file_path = filedialog.asksaveasfilename(
                        initialdir = Organizer.app_dir,
                        title = 'Save as?',
                        defaultextension = '.wtl')

        if file_path != '':
            self.controller.save_as(file_path)


