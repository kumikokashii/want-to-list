from .incremental_id_list import *
from .contact_info import *
from .phone import *
from .address import *

class ContactInfoBook(IncrementalIDList):
    def __init__(self):
        super().__init__()

    def add_contact_info(self, name, phone=None, address=None):
        id = self.get_next_id()
        contact_info = ContactInfo(id, name, phone, address)
        self.append(contact_info)

    def set_default(self):
        self.clear()
        self.add_contact_info(name='7Eleven', 
                              phone=Phone('7117117117'), 
                              address=Address('711 Fun St', 'Dream Land', 'CA', '71171'))
