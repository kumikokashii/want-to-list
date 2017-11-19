import os
import sys

from .item_type_list import *
from .priority_list import *
from .contact_info_book import *
from .item_list import *

from .money import *

import pickle

class Organizer():
    up2dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_file_path = up2dir + '/my_want_to_list.pickle'
    file_of_path_to_last_saved = up2dir + '/.want_to_list_data'

    def __init__(self):
        self.item_type_list = ItemTypeList.get_default()
        self.priority_list = PriorityList()
        self.contact_info_book = ContactInfoBook()
        self.item_list = ItemList(self.item_type_list, self.priority_list, self.contact_info_book)
        self.file_path = self.get_file_path()

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

    def get_file_path(self):
        if os.path.isfile(Organizer.file_of_path_to_last_saved):
            with open(Organizer.file_of_path_to_last_saved, 'r') as f:
                return f.read()

        # If no hidden file, use default 
        return Organizer.default_file_path

    def load(self, file_path=default_file_path):
        if not os.path.isfile(file_path):  # Do nothing if no such file
            print('nothing', file_path)  # TEST
            return

        with open(file_path, 'rb') as f:
            new_organizer = pickle.load(f)
        self.item_type_list = new_organizer.item_type_list
        self.priority_list = new_organizer.priority_list
        self.contact_info_book = new_organizer.contact_info_book
        self.item_list = new_organizer.item_list
        self.file_path = file_path
        print('loaded', file_path)  # TEST

    def save(self, as_file_path=None):
        if as_file_path is not None:
            self.file_path = as_file_path
        with open(self.file_path, 'wb') as f:
            pickle.dump(self, f)  # Save pickle

        with open(Organizer.file_of_path_to_last_saved, 'w') as f:
            f.write(self.file_path)  # Update path to pickle in hidden file

    def remove_contact_info(self, id):
        self.item_list.remove_contact_info(id)
        self.contact_info_book.remove_elem_by_id(id)

    def remove_priority(self, id):
        self.item_list.remove_priority(id)
        self.priority_list.remove_elem_by_id(id)

    def start_fresh(self):
        for lst in [self.priority_list, self.contact_info_book, self.item_list]:
            lst.clear()

    def get_test_instance():
        organizer = Organizer()

        l = organizer.item_list
        l.add_item(name='Eat', due_date=date(2017, 11, 11))
        l.add_item(name='Sleep', priority=organizer.priority_list.get_elem_by_id(0))
        l.add_item(name='Drink')
        l.add_item(name='Talk', contact_info=organizer.contact_info_book.get_elem_by_id(0))
        l.add_item(name='Walk', is_checked=True)
        l.add_item(name='Shrimp', parent=l.get_elem_by_name('Eat'))
        l.add_item(name='Crab', parent=l.get_elem_by_name('Eat'))
        l.add_item(name='Lobster', parent=l.get_elem_by_name('Eat'))
        l.add_item(name='Michelada', parent=l.get_elem_by_name('Drink'), money=Money(3.50))
        l.add_item(name='Sake', parent=l.get_elem_by_name('Drink'), money=Money(27))
        l.add_item(name='Hot Sake', parent=l.get_elem_by_name('Sake'), money=Money(11))
        l.add_item(name='Cold Sake', parent=l.get_elem_by_name('Sake'), money=Money(12.3))

        return organizer
