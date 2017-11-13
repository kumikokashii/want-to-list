from .incremental_id_list import *
from .contact_info import *
from .phone import *
from .address import *

class ContactInfoBook(IncrementalIDList):
    def get_test_instance():
        contact_info_book = ContactInfoBook()
        contact_info_book.add_contact_info(name='7Eleven', phone_digits='7117117117', 
                                           street_address='711 Fun St', 
                                           city='Dream Land', state='CA', zip_code='71171')
        contact_info_book.add_contact_info(name='Turkey', city='Fun City')
        contact_info_book.add_contact_info(name='Mario', phone_digits='   3334444', city='Nintendo') 
        contact_info_book.add_contact_info(name='Donkey Kong', phone_digits='5555555555', city='Nintendo') 
        return contact_info_book

    def __init__(self):
        super().__init__()

    def add_contact_info(self, name, phone_digits='', street_address='', city='', state='', zip_code=''):
        id = self.get_next_id()
        phone = Phone(phone_digits)
        address = Address(street_address, city, state, zip_code)
        contact_info = ContactInfo(id, name, phone, address)
        self.append(contact_info)

    def get_sorted_by_name(self):
        return sorted(self, key=lambda contact_info: contact_info.name)
