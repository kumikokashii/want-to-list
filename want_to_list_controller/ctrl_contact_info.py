
from want_to_list_model import *

class CTRLContactInfo():
    def __init__(self, organizer, ui):
        self.item_list = organizer.item_list
        self.contact_info_book = organizer.contact_info_book
        self.ui = ui

    def format_entries(self, entries):
        contact_info = {}
        for field, input in entries.items():
            contact_info[field] = input.get()

        name = contact_info['name']
        phone = Phone(contact_info['phone'])
        address = Address(contact_info['street address'], contact_info['city'], contact_info['state'], contact_info['zip code'])
        return name, phone, address 

    def add(self, entries):
        # Add new contact info to organizer
        name, phone, address = self.format_entries(entries)
        self.contact_info_book.add_contact_info(name=name, phone=phone, address=address)

        # Refresh Contact Info View
        self.ui.contact_info.refresh_view()

        # Go to Contact Info View
        pass

    def remove(self, id):
        # Remove contact info from organizer
        self.item_list.remove_contact_info(id)
        self.contact_info_book.remove_elem_by_id(id)

        # Refresh Contact Info View
        self.ui.contact_info.refresh_view()

        # Refresh Item List 
        self.ui.item_list.refresh_right()

