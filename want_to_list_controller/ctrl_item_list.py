from datetime import datetime, date

class CTRLItemList():
    def __init__(self, organizer, ui):
        self.item_list = organizer.item_list
        self.priority_list = organizer.priority_list
        self.contact_info_book = organizer.contact_info_book
        self.ui = ui.item_list

    def toggle_check(self, id):
        # Toggle check for item in organizer
        item = self.item_list.get_elem_by_id(id)
        item.toggle_check()

        # Refresh Item List
        self.ui.refresh_left()
        #self.ui.refresh_right()

    def onclick_item(self, id):
        item = self.item_list.get_elem_by_id(id)

        if len(item) > 0:  # If there are children items, show them on Left
            self.ui.current_list = item
            self.ui.refresh_left()

        # Show self details on Right
        self.ui.current_item = item
        self.ui.refresh_right()

    def onclick_title(self, id):
        item = self.item_list.get_elem_by_id(id)
        self.ui.current_item = item
        self.ui.refresh_right()

    def add_item(self, name):
        parent = self.ui.current_list  # Can i do this?
        item = self.item_list.add_item(name=name, parent=parent)

        self.ui.refresh_left()
        self.ui.current_item = item
        self.ui.refresh_right()

    def add_child(self, name):
        parent = self.ui.current_item
        item = self.item_list.add_item(name=name, parent=parent)

        self.ui.current_list = self.ui.current_item
        self.ui.refresh_left()
        self.ui.current_item = item
        self.ui.refresh_right()

    def update_item(self, id, values):
        item = self.item_list.get_elem_by_id(id)

        # Name
        name = values['Name']
        item.update_name(name)

        # Due Date
        date_dict = values['Due']
        if date_dict is None:
            due_date = None
        else:
            due_date = date(date_dict['Year'], date_dict['Month'], date_dict['Day'])
        item.update_due_date(due_date)

        # Priority
        priority_name = values['Priority']
        priority = self.priority_list.get_elem_by_name(priority_name)
        item.update_priority(priority)

        # Picture
        #item.picture = values['Img']

        # Money
        amount = values['Money']
        item.update_money_amount(amount)

        # Contact Info
        contact_info_name = values['Contact Info']
        contact_info = self.contact_info_book.get_elem_by_name(contact_info_name)
        item.update_contact_info(contact_info)

        # Refresh
        self.ui.refresh_left()
        self.ui.refresh_right()
