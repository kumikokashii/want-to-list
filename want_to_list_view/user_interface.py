from tkinter import *
from tkinter import ttk

from want_to_list_view import *

class UserInterface(Tk):
    def __init__(self, organizer):
        super().__init__()
        
        self.title('Want To List')
        self.geometry('800x500')

        self.nb = ttk.Notebook(self)
        self.nb.grid()  # Need to specify parameters???
        
        self.item_list = UIItemList(parent=self.nb, tab_name='Item List', organizer=organizer) 
        self.contact_info = UIContactInfo(parent=self.nb, tab_name='Contact Info', contact_info_book=organizer.contact_info_book)
        self.priorities = UIPriorities(parent=self.nb, tab_name='Priorities', priority_list=organizer.priority_list)

    def set_controller(self, controller):
        self.controller = controller
        self.item_list.controller = controller.item_list
        self.contact_info.controller = controller.contact_info
        self.priorities.controller = controller.priorities

    def initialize(self):
        self.item_list.refresh_left()
        self.contact_info.refresh_view()
        self.contact_info.refresh_add()
        self.priorities.refresh()

