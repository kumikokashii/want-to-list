
class CTRLItemList():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.item_list = organizer.item_list
        self.ui = ui

    def check_item(self, id):
        # Remove item from organizer
        self.item_list.remove_elem_by_id(id)

        # Refresh Item List
        self.ui.item_list.refresh_left()
        #self.ui.item_list.refresh_right()

    def onclick_item(self, id):
        print(id)

        # If item has children, show children on Left
        # Show self details on Right
