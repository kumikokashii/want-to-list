from .incremental_id_list import *
from .item_type import *

class ItemTypeList(IncrementalIDList):
    def __init__(self):
        super().__init__()

    def add_item_type(self, name):
        id = self.get_next_id()
        item_type = ItemType(id, name)
        self.append(item_type)

    def set_default(self):
        self.clear()
        self.add_item_type('check')
        self.add_item_type('note')

