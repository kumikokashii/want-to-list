from .incremental_id_list import *
from .item_type import *

class ItemTypeList(IncrementalIDList):
    def __init__(self):
        super().__init__()

    def add_item_type(self, name):
        id = self.get_next_id()
        item_type = ItemType(id, name)
        self.append(item_type)

    def get_default():
        item_type_list = ItemTypeList()
        item_type_list.add_item_type('check')
        item_type_list.add_item_type('note')
        return item_type_list

