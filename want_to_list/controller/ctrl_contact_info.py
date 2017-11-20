from ..str_vars import *

class CTRLContactInfo():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.ui = ui

    def add(self, values):
        # Add new contact info to organizer
        name = values[name_]
        phone_digits = values[phone_]
        street_address = values[street_address_]
        city = values[city_]
        state = values[state_]
        zip_code = values[zip_code_]
        self.organizer.contact_info_book.add_contact_info(name, phone_digits, street_address, city, state, zip_code)

        # Refresh Contact Info View & Add
        self.ui.contact_info.refresh_view()
        self.ui.contact_info.refresh_add()

        # Go to Contact Info View
        pass

    def remove(self, id):
        # Remove contact info from organizer
        self.organizer.remove_contact_info(id)

        # Refresh Contact Info View
        self.ui.contact_info.refresh_view()

        # Refresh Item List 
        self.ui.item_list.refresh_item()

