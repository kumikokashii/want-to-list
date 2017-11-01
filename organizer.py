from item_type_list import *
from priority_list import *
from contact_info_book import *
from list import *

class Organizer():
    def __init__(self):
        self.item_type_list = ItemTypeList()
        self.priority_list = PriorityList()
        self.contact_info_book = ContactInfoBook()
        self.list = List(self.item_type_list)
    
    def load_default(self):
        self.item_type_list.set_default()
        self.priority_list.set_default()
        self.contact_info_book.set_default()
        self.list.set_default()

    def load(self):
        pass
