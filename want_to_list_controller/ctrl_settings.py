
class CTRLSettings():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.ui = ui

    def save_exit(self):
        self.organizer.save()
        self.ui.destroy()

    def start_fresh(self):
        self.organizer.start_fresh()

        self.ui.item_list.current_list = self.organizer.item_list.root
        self.ui.item_list.current_item = self.organizer.item_list.root

        self.ui.initialize()
