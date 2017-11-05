
class CTRLItemList():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.item_list = organizer.item_list
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
        parent = self.ui.current_list
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


