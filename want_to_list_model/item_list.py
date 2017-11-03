from .incremental_id_list import *
from datetime import datetime
from .item import *

class ItemList(IncrementalIDList):
    def __init__(self, item_type_list):
        super().__init__()
        self.item_type_list = item_type_list

    def add_item(self, name, item_type=None, parent_item=None, 
                 due_date=None, priority=None, picture=None, money=0, contact_info=None):
        id = self.get_next_id()
        created_date = datetime.today().date()
        if item_type is None:
            item_type = self.item_type_list.get_elem_by_name('check')
        item = Item(id, name, item_type, parent_item, 
                    created_date, due_date, priority, picture, 
                    money, contact_info)
        self.append(item)

    def set_default(self):
        self.clear()
        self.add_item(name='Eat')
        self.add_item(name='Sleep')

