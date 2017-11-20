from .incremental_id_list import *
from .contact_info import *
from .phone import *
from .address import *

class ContactInfoBook(IncrementalIDList):
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
