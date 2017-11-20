
from tkinter import ttk
from PIL import Image, ImageTk

from ..str_vars import *

class UIFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def cleanup(self):
        for widget in self.winfo_children():
            widget.destroy()

    def get_label_dict(self, frame, text_list):
        label = {}
        for text in text_list:
            label[text] = ttk.Label(frame, text=text)
        return label

    def get_item_name(self, item, show):
        name = item.name 
        if show == 'current list only':
            return name
        parent = item.parent
        if parent.id == 0:  # If top level
            return name
        return name + ' [' + parent.name + ']'

    def get_item_dict(self, item):
        item_dict = {name_: item.name,
                     due_date_: item.due_date,
                     priority_: item.priority,
                     picture_: item.picture,
                     money_: item.money,
                     contact_info_: item.contact_info,
                     created_date_: item.created_date}
        return item_dict

    def get_resized_tk_image(self, pil_image, side_max):
        image = pil_image.copy()
        image.thumbnail((side_max, side_max), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

class UITabInNB(UIFrame):
    def __init__(self, parent, tab_name):
        super().__init__(parent)
        parent.add(self, text=tab_name)

