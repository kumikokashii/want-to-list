from priority import *

class PriorityList():
    def __init__(self):
        self.list = []

    def __str__(self):
        output = ''
        for priority in self.list:
            output += priority.concat()
            output += '\n'
        return output 

    def add(self, priority):
        self.list.append(priority)

    def get_priority_by_id(self, id):
        for priority in self.list:
            if priority.id == id:
                return priority
        return None

    def edit(self, new_list):
        # new_list is a user input. It's a tuple of tuples. ((id, name, importance), ...)
        
        new_priority_list = []
        for new_priority in new_list:
            new_id, new_name, new_importance = new_priority

            priority = self.get_priority_by_id(new_id)
            if priority:
                # If id exists, overwrite name and importance
                priority.name = new_name
                priority.importance = new_importance
                new_priority_list.append(priority)
            else:
                # If id doesn't exist, create a new priority
                new_priority_list.append(Priority(new_id, new_name, new_importance))

        self.list = new_priority_list

