
class CTRLItemList():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.item_list = organizer.item_list
        self.ui = ui

    def toggle_check(self, id):
        # Toggle check for item in organizer
        item = self.item_list.get_elem_by_id(id)
        item.toggle_check()

        # Refresh Item List
        self.ui.item_list.refresh_left()
        #self.ui.item_list.refresh_right()

    def onclick_item(self, id):
        item = self.item_list.get_elem_by_id(id)

        # If there are children items, show them on Left
        if len(item) > 0:
            self.ui.item_list.current_list = item
            self.ui.item_list.refresh_left()

        # Show self details on Right
        self.ui.item_list.current_item = item
        self.ui.item_list.refresh_right()

    def onclick_title(self, id):
        item = self.item_list.get_elem_by_id(id)
        self.ui.item_list.current_item = item
        self.ui.item_list.refresh_right()
