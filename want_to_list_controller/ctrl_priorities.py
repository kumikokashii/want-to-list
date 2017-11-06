
class CTRLPriorities():
    def __init__(self, organizer, ui):
        self.item_list = organizer.item_list
        self.priority_list = organizer.priority_list
        self.ui = ui

    def edit(self, values):
        # Update priority in organizer
        self.priority_list.edit(values)

        self.refresh_ui()

    def remove(self, id):
        # Remove priority from organizer
        self.item_list.remove_priority(id)
        self.priority_list.remove_elem_by_id(id)

        self.refresh_ui()

    def refresh_ui(self):
        # Refresh Priorities
        self.ui.priorities.refresh()

        # Refresh Item List
        self.ui.item_list.refresh_right()

