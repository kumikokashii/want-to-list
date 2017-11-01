from incremental_id_list import *
from priority import *

class PriorityList():
    def __init__(self):
        self.list = IncrementalIDList()

    def __str__(self):
        return str(self.list)

    def add_priority(self, name, importance):
        id = self.list.get_next_id()
        priority = Priority(id, name, importance) 
        self.list.append(priority)

    def edit(self, new_list):
        # new_list is a user input. It's a tuple of tuples. ((id, name, importance), ...)
        
        new_priority_list = IncrementalIDList()
        for new_priority in new_list:
            new_id, new_name, new_importance = new_priority

            priority = self.list.get_elem_by_id(new_id)
            if priority:
                # If id exists, overwrite name and importance
                priority.name = new_name
                priority.importance = new_importance
                new_priority_list.append(priority)
            else:
                # If id doesn't exist, create a new priority
                new_priority_list.append(Priority(new_id, new_name, new_importance))

        self.list = new_priority_list

    def set_default(self):
        self.list = IncrementalIDList()
        self.add_priority(name='high', importance=1)
        self.add_priority(name='normal', importance=2)
        self.add_priority(name='low', importance=3)
