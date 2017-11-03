
class CTRLPriorities():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.priority_list = organizer.priority_list
        self.ui = ui

    def format_entries(self):
        pass

    def remove(self, id):
        # Remove priority from organizer
        self.priority_list.remove_elem_by_id(id)

        # Refresh Priorities
        self.ui.priorities.refresh()

        # Refresh Item List View and Item List Add
        pass
