from .incremental_id_list import *
from .contact_info import *

class ContactInfoBook():
    def __init__(self):
        self.book = IncrementalIDList()

    def __str__(self):
        return str(self.book)

    def add_contact_info(self, name, phone=None, address=None):
        id = self.book.get_next_id()
        contact_info = ContactInfo(id, name, phone, address)
        self.book.append(contact_info)

    def set_default(self):
        self.book = IncrementalIDList()
        self.add_contact_info(name='7Eleven', phone='7117117117', address=None)
