
from .ui_tab_in_notebook import *
from .ui_show_list import *
from .ui_show_item import *
from .ui_edit_item import *

class UIItemList(UITabInNB):
    def __init__(self, parent, tab_name, organizer): 
        super().__init__(parent, tab_name)
        self.controller = None
        self.item_list = organizer.item_list
        self.priority_list = organizer.priority_list
        self.contact_info_book = organizer.contact_info_book
        self.show = 'current list only'
        self.frame_show_list = UIShowList(self)
        self.frame_show_item = UIShowItem(self)
        self.frame_edit_item = UIEditItem(self)

    def refresh_list(self, new_list=None):
        self.frame_show_list.refresh(new_list)
        self.frame_show_list.grid(row=0, column=0, sticky=N)
        
    def refresh_item(self, item=None):
        self.frame_show_item.refresh(item)
        self.frame_edit_item.grid_remove()
        self.frame_show_item.grid(row=0, column=1, sticky=N)

    def edit_item_mode(self, item):
        self.frame_edit_item.refresh(item)
        self.frame_show_item.grid_remove()
        self.frame_edit_item.grid(row=0, column=1, sticky=N)



