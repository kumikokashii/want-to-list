from .item_type_list import *
from .priority_list import *
from .contact_info_book import *
from .item_list import *

from .money import *

import pickle

class Organizer():
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

    def __init__(self):
        self.item_type_list = ItemTypeList.get_default()
        self.priority_list = PriorityList.get_test_instance()
        self.contact_info_book = ContactInfoBook.get_test_instance()
        self.item_list = ItemList(self.item_type_list, self.priority_list, self.contact_info_book)

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

    def add_contact_info(self, name, phone_digits, street_address, city, state, zip_code):
        phone = Phone(phone_digits)
        address = Address(street_address, city, state, zip_code)
        self.contact_info_book.add_contact_info(name, phone, address)

    def remove_contact_info(self, id):
        self.item_list.remove_contact_info(id)
        self.contact_info_book.remove_elem_by_id(id)

    def edit_priorities(self, values):
        self.priority_list.edit(values)

    def remove_priority(self, id):
        self.item_list.remove_priority(id)
        self.priority_list.remove_elem_by_id(id)



