
from tkinter import ttk

class UIFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def cleanup(self):
        for widget in self.winfo_children():
            widget.destroy()

class UITabInNB(UIFrame):
    def __init__(self, parent, tab_name):
        super().__init__(parent)
        parent.add(self, text=tab_name)

