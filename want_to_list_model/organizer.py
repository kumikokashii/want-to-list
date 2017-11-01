from .item_type_list import *
from .priority_list import *
from .contact_info_book import *
from .list import *

import pickle

class Organizer():
    def __init__(self):
        self.item_type_list = ItemTypeList()
        self.priority_list = PriorityList()
        self.contact_info_book = ContactInfoBook()
        self.list = List(self.item_type_list)

    def __str__(self):
        output = ''
        output += '-' * 10 + 'Item Types' + '-' * 10
        output += '\n'
        output += str(self.item_type_list)
        output += '-' * 10 + 'Priorities' + '-' * 10
        output += '\n'
        output += str(self.priority_list)
        output += '-' * 10 + 'Contact Info' + '-' * 10
        output += '\n'
        output += str(self.contact_info_book)
        output += '-' * 10 + 'Items' + '-' * 10
        output += '\n'
        output += str(self.list)
        return output
    
    def load_default(self):
        self.item_type_list.set_default()
        self.priority_list.set_default()
        self.contact_info_book.set_default()
        self.list.set_default()

    def load(self):
        with open('want_to_list.pickle', 'rb') as f:
            return pickle.load(f)

    def save(self):
        with open('want_to_list.pickle', 'wb') as f:
            pickle.dump(self, f)


