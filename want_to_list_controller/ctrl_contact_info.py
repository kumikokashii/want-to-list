from str_vars import *
from want_to_list_model import *

class CTRLContactInfo():
    def __init__(self, organizer, ui):
        self.item_list = organizer.item_list
        self.contact_info_book = organizer.contact_info_book
        self.ui = ui

    def add(self, values):
        # Add new contact info to organizer
        name = values[name_]
        phone = Phone(values[phone_])
        address = Address(values[street_address_], values[city_], values[state_], values[zip_code_])
        self.contact_info_book.add_contact_info(name=name, phone=phone, address=address)

        # Refresh Contact Info View & Add
        self.ui.contact_info.refresh_view()
        self.ui.contact_info.refresh_add()

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

