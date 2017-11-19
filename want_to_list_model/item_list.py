from .incremental_id_list import *
from .item_list_element import *
from datetime import datetime, date

from str_vars import *

class ItemList(IncrementalIDList):
    def __init__(self, item_type_list, priority_list, contact_info_book):
        super().__init__()
        self.set_root()
        self.item_type_list = item_type_list
        self.priority_list = priority_list
        self.contact_info_book = contact_info_book

    def clear(self):
        super().clear()
        self.root.clear()
        self.append(self.root)

    def set_root(self):
        id = self.get_next_id()
        created_date = datetime.today()

        item = ItemListElement(id=id, name='Root', item_type=None, parent=None, 
                               created_date=created_date, due_date=None, priority=None, picture=None, 
                               money=None, contact_info=None, is_checked=False)
        self.append(item)
        self.root = item

    def add_item(self, name, item_type=None, parent=None, 
                 due_date=None, priority=None, picture=None, money=None, 
                 contact_info=None, is_checked=False):

        id = self.get_next_id()
        created_date = datetime.today()
        if item_type is None:
            item_type = self.item_type_list.get_elem_by_name('check')
        if parent is None:
            parent = self.root

        item = ItemListElement(id, name, item_type, parent, 
                               created_date, due_date, priority, picture, 
                               money, contact_info, is_checked)
        self.append(item)

        # Add to parent's list, refresh parent's money amount total
        parent.append(item)
        parent.refresh_money_amount_self_and_parents()

        return item

    def remove_children_and_self(self, item):
        if len(item) > 0:
            for child_item in item:  # Remove all children
                self.remove_children_and_self(child_item)
        self.remove(item)  # Remove self

    def remove_item(self, id):
        item = self.get_elem_by_id(id)
        parent = item.parent

        item.parent.remove(item)  # Out of parent list
        self.remove_children_and_self(item)
        parent.refresh_money_amount_self_and_parents()

    def remove_contact_info(self, id):
        contact_info = self.contact_info_book.get_elem_by_id(id)        
        for item in self:
            if item.contact_info is contact_info:  # is checkes references pointed. == checks values.
                item.contact_info = None

    def remove_priority(self, id):
        priority = self.priority_list.get_elem_by_id(id)        
        for item in self:
            if item.priority is priority:  # is checkes references pointed. == checks values.
                item.priority = None

    def toggle_check(self, id):
        item = self.get_elem_by_id(id)
        item.toggle_check()

    def update_item(self, id, name, due_date, priority_name,
                    picture_skip_update, picture, amount, contact_info_name):
        item = self.get_elem_by_id(id)

        item.update_name(name)
        item.update_due_date(due_date)
        item.update_priority(self.priority_list.get_elem_by_name(priority_name))
        if not picture_skip_update:
            item.update_picture(picture)
        item.update_money_amount(amount)
        item.update_contact_info(self.contact_info_book.get_elem_by_name(contact_info_name))


