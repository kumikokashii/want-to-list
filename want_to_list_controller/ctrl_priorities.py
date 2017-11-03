
class CTRLPriorities():
    def __init__(self, organizer, ui):
        self.organizer = organizer
        self.priority_list = organizer.priority_list
        self.ui = ui

    def format_entries(self, entries):
        new_list = []
        for id, name_importance_entries in entries.items():
            name_entry, importance_entry = name_importance_entries
            name = name_entry.get()
            importance = importance_entry.get()
            print(id, name, importance)
            if id == 'new':
                # New priority row
                continue  # Check if its legit
            
            new_list.append((id, name, importance))
        return new_list

    def edit(self, entries):
        new_list = self.format_entries(entries)
        self.priority_list.edit(new_list)
        self.ui.priorities.refresh()

    def get_remove_by_id_func(self, id):
        def remove():
            self.remove(id)
        return remove

    def remove(self, id):
        # Remove priority from organizer
        self.priority_list.remove_elem_by_id(id)

        # Refresh Priorities
        self.ui.priorities.refresh()

        # Refresh Item List View and Item List Add
        pass
