from .incremental_id_list import *
from datetime import datetime, date
from .item import *

class ItemList(IncrementalIDList):
    def __init__(self, item_type_list):
        super().__init__()
        self.item_type_list = item_type_list

    def get_sorted_by(self, key):
        if key == 'name':
            return sorted(self, key=lambda item: item.name)
        if key == 'created date':
            return sorted(self, key=lambda item: item.created_date)
        if key == 'due date':
            return sorted(self, key=lambda item: item.due_date)
        if key == 'priority':
            return sorted(self, key=lambda item: item.priority)

    def add_item(self, name, item_type=None, parent=None, 
                 due_date=None, priority=None, picture=None, money=0, 
                 contact_info=None, is_checked=False):
        id = self.get_next_id()
        created_date = datetime.today()
        if item_type is None:
            item_type = self.item_type_list.get_elem_by_name('check')
        item = Item(id, name, item_type, parent,
                    created_date, due_date, priority, picture, 
                    money, contact_info, is_checked)
        self.append(item)

        # Add item to parent's children
        if parent is not None:
            parent.add_child(item)

    def set_default(self):
        self.clear()
        self.add_item(name='Eat', is_checked=True, due_date=date(2017, 11, 11))
        self.add_item(name='Sleep', parent=self.get_elem_by_id(0))
        self.add_item(name='Drink', parent=self.get_elem_by_id(0))

