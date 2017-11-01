from .incremental_id_list import *
from datetime import datetime
from .item import *

class List():
    def __init__(self, item_type_list):
        self.list = IncrementalIDList()
        self.item_type_list = item_type_list

    def __str__(self):
        return str(self.list)

    def add_item(self, name, item_type=None, parent_item=None, 
                 due_date=None, priority=None, picture=None, money=0, contact_info=None):
        id = self.list.get_next_id()
        created_date = datetime.today().date()
        if item_type is None:
            item_type = self.item_type_list.list.get_elem_by_name('check')
        item = Item(id, name, item_type, parent_item, 
                    created_date, due_date, priority, picture, 
                    money, contact_info)
        self.list.append(item)

    def set_default(self):
        self.list = IncrementalIDList()
        self.add_item(name='Eat')
        self.add_item(name='Sleep')

