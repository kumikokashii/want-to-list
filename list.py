from datetime import datetime
from item import *

class List():
    def __init__(self):
        self.list = []

    def __str__(self):
        output = ''
        for item in self.list:
            output += str(item)
            output += '\n'
        return output

    def get_next_id(self):
        max_id = -1
        for item in self.list:
            if item.id > max_id:
                max_id = item.id
        return max_id + 1

    def add_item(self, name, item_type, parent_item, 
                 due_date, priority, picture, money, contact_info):
        id = self.get_next_id()
        created_date = datetime.today().date()
        item = Item(id, name, item_type, parent_item, 
                    created_date, due_date, priority, picture, 
                    money, contact_info)
        self.list.append(item)
