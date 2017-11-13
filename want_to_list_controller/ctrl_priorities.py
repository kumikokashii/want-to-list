
class CTRLPriorities():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.ui = ui

    def edit(self, values):
        # Update priority in organizer
        self.organizer.priority_list.edit(values)

        self.refresh_ui()

    def remove(self, id):
        # Remove priority from organizer
        self.organizer.remove_priority(id)

        self.refresh_ui()

    def refresh_ui(self):
        # Refresh Priorities
        self.ui.priorities.refresh()

        # Refresh Item List
        self.ui.item_list.refresh_list()
        self.ui.item_list.refresh_item()
