from list import *
from priority_list import *
from contact_info_book import *

class Organizer():
    def __init__(self):
        self.list = List()
        self.priority_list = PriorityList()
        self.contact_info_book = ContactInfoBook()

    def load_default(self):
        self.list.set_default()
        self.priority_list.set_default()
        self.contact_info_book.set_default()

    def load(self):
        pass
