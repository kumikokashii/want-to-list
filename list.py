from datetime import datetime
from item import *

class List():
    def __init__(self, item_type_list):
        self.list = []
        self.item_type_list = item_type_list

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

    def add_item(self, name, item_type=None, parent_item=None, 
                 due_date=None, priority=None, picture=None, money=0, contact_info=None):
        id = self.get_next_id()
        created_date = datetime.today().date()
        if item_type is None:
            item_type = self.item_type_list.get_item_type_by_name('check')
        item = Item(id, name, item_type, parent_item, 
                    created_date, due_date, priority, picture, 
                    money, contact_info)
        self.list.append(item)

    def set_default(self):
        self.list = []
        self.add_item(name='Eat')
        self.add_item(name='Sleep')

