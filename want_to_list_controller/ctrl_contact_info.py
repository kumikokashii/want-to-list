from str_vars import *
from want_to_list_model import *

class CTRLContactInfo():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.ui = ui

    def add(self, values):
        # Add new contact info to organizer
        name = values[name_]
        phone = Phone(values[phone_])
        address = Address(values[street_address_], values[city_], values[state_], values[zip_code_])
        self.organizer.add_contact_info(name, phone, address)

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
        self.ui.item_list.refresh_right()

