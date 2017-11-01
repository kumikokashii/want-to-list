from incremental_id_list import *
from item_type import *

class ItemTypeList():
    def __init__(self):
        self.list = IncrementalIDList() 

    def __str__(self):
        return str(self.list)

    def add_item_type(self, name):
        id = self.list.get_next_id()
        item_type = ItemType(id, name)
        self.list.append(item_type)

    def set_default(self):
        self.list = IncrementalIDList()
        self.add_item_type('check')
        self.add_item_type('note')

