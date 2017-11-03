from tkinter import *
from tkinter import ttk

from ui_item_list import *
from ui_contact_info import *
from ui_priorities import *

class UserInterface(Tk):
    def __init__(self, organizer):
        super().__init__()
        
        self.title('Want To List')
        self.geometry('800x500')

        self.nb = ttk.Notebook(self)
        self.nb.grid()  # Need to specify parameters???
        
        self.item_list = UIItemList(parent=self.nb, tab_name='Item List', item_list=organizer.item_list)
        self.contact_info = UIContactInfo(parent=self.nb, tab_name='Contact Info', contact_info_book=organizer.contact_info_book)
        self.priorities = UIPriorities(parent=self.nb, tab_name='Priorities', priority_list=organizer.priority_list)

    def initialize(self):
        self.item_list.refresh_view()
        self.contact_info.refresh_view()
        self.contact_info.initialize_add()
        self.mainloop()

