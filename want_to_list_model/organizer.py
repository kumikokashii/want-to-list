from .item_type_list import *
from .priority_list import *
from .contact_info_book import *
from .item_list import *

import pickle

class Organizer():
    def get_test_instance():
        organizer = Organizer()

        organizer.priority_list = PriorityList.get_test_instance()
        organizer.contact_info_book = ContactInfoBook.get_test_instance()

        organizer.item_list.add_item(name='Eat')
        organizer.item_list.add_item(name='Sleep')
        organizer.item_list.add_item(name='Drink')
        organizer.item_list.add_item(name='Talk')

        return organizer

    def __init__(self):
        self.item_type_list = ItemTypeList.get_default()
        self.priority_list = PriorityList()
        self.contact_info_book = ContactInfoBook()
        self.item_list = ItemList(self.item_type_list)

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
        output += str(self.item_list)
        return output
    

    def load(self):
        with open('want_to_list.pickle', 'rb') as f:
            return pickle.load(f)

    def save(self):
        with open('want_to_list.pickle', 'wb') as f:
            pickle.dump(self, f)


