from datetime import datetime, date

from ..str_vars import *

class CTRLItemList():
    def __init__(self, organizer, ui):
        self.item_list = organizer.item_list
        self.priority_list = organizer.priority_list
        self.contact_info_book = organizer.contact_info_book
        self.ui = ui.item_list

    def toggle_check(self, id):
        # Toggle check for item in organizer
        self.item_list.toggle_check(id)

        # Refresh Item List
        self.ui.refresh_list()
        #self.ui.refresh_item()

    def onclick_item(self, id):
        item = self.item_list.get_elem_by_id(id)

        if len(item) > 0:  # If there are children items, show them on Left
            self.ui.refresh_list(item)

        # Show self details on Right
        self.ui.refresh_item(item)

    def onclick_title(self, id):
        item = self.item_list.get_elem_by_id(id)
        self.ui.refresh_item(item)

    def add_item(self, name, parent):
        item = self.item_list.add_item(name=name, parent=parent)

        self.ui.refresh_list()
        self.ui.refresh_item(item)

    def add_child(self, name, parent):
        item = self.item_list.add_item(name=name, parent=parent)

        self.ui.refresh_list(parent)
        self.ui.refresh_item(item)

    def update_item(self, id, values):

        # Name
        name = values[name_]

        # Due Date
        date_dict = values[due_date_]
        if date_dict is None:
            due_date = None
        else:
            due_date = date(date_dict[year_], date_dict[month_], date_dict[day_])

        # Priority
        priority_name = values[priority_]

        # Picture
        picture_skip_update, picture = values[picture_]

        # Money
        amount = values[money_]

        # Contact Info
        contact_info_name = values[contact_info_]

        # Send to organizer
        self.item_list.update_item(id, name, due_date, priority_name,
                                   picture_skip_update, picture, amount, contact_info_name) 

        # Refresh UI
        self.ui.refresh_list()
        self.ui.refresh_item()

    def remove_item(self, id): 
        item = self.item_list.get_elem_by_id(id)
        new_left = item.parent if (len(item) > 0) else None
        self.item_list.remove_item(id)

        self.ui.refresh_list(new_left)
        self.ui.refresh_item(self.item_list.root)

