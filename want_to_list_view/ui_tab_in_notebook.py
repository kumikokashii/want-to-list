
from tkinter import ttk

class UITabInNB(ttk.Frame):
    def __init__(self, parent, tab_name):
        super().__init__(parent)
        parent.add(self, text=tab_name)

    def cleanup(self):
        for widget in self.winfo_children():
            widget.destroy()

