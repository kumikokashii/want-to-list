
from tkinter import *
from tkinter import ttk

class UIFrame(ttk.Frame):
    def __init__(self, parent):
        style = ttk.Style()
        style.theme_use('classic')
        style.configure('TFrame', background='white')

        super().__init__(parent)

    def cleanup(self):
        for widget in self.winfo_children():
            widget.destroy()

    def get_label_dict(self, frame, text_list):
        label = {}
        for text in text_list:
            label[text] = Label(frame, text=text)
        return label

class UITabInNB(UIFrame):
    def __init__(self, parent, tab_name):
        super().__init__(parent)
        parent.add(self, text=tab_name)

