from .incremental_id_list import *
from .priority import *

class PriorityList(IncrementalIDList):
    def __init__(self):
        super().__init__()

    def add_priority(self, name, importance):
        id = self.get_next_id()
        priority = Priority(id, name, importance) 
        self.append(priority)

    def get_sorted_by_importance(self):
        return sorted(self, key=lambda priority: priority.importance)

    def edit(self, new_list):
        # new_list is a user input. It's a tuple of tuples. ((id, name, importance), ...)
        
        current_list = self.copy()
        self.clear()

        for new_priority in new_list:
            new_id, new_name, new_importance = new_priority

            priority = current_list.get_elem_by_id(new_id)
            if priority:
                # If id exists, overwrite name and importance
                priority.name = new_name
                priority.importance = new_importance
                self.append(priority)
            else:
                # If id doesn't exist, create a new priority
                self.append(Priority(new_id, new_name, new_importance))

    def set_default(self):
        self.clear()
        self.add_priority(name='high', importance=1)
        self.add_priority(name='normal', importance=2)
        self.add_priority(name='low', importance=3)
