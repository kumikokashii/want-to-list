
from .incremental_id_list import *

class Item():
    def __init__(self, id, name, item_type, parent,  
                 created_date, due_date, priority, picture, 
                 money, contact_info, is_checked=False):
        self.id = id  # int
        self.name = name  # str
        self.item_type = item_type  # ItemType
        self.parent = parent  # Item
        self.children = IncrementalIDList()  # IncrementalIDList
        self.created_date = created_date  # date
        self.due_date = due_date  # date
        self.priority = priority  # Priority
        self.picture = picture  # Picture
        self.money = money  # Money
        self.contact_info = contact_info  # ContactInfo
        self.is_checked = is_checked  # boolean

    def __str__(self):
        attribute_names = ['ID', 'Name', 'Type', 'Parent', 'Children', 'Checked', 
                           'Created Date', 'Due Date', 'Prority', 'Picture', 
                           'Money', 'Contact Info']
        attribute_vars = [self.id, self.name, self.item_type, self.parent,
                          self.children, self.is_checked, 
                          self.created_date, self.due_date, self.priority, self.picture, 
                          self.money, self.contact_info]
        output = ''
        for i in range(len(attribute_names)):
            output += attribute_names[i] + ': '
            if attribute_vars[i] is not None:
                if attribute_names[i] in ['Parent', 'Children']:
                    output += attribute_vars[i].short_str()
                else:
                    output += str(attribute_vars[i])
            else:
                output += 'None'
            output += '\n'
        return output

    def short_str(self):
        return str(self.id) + ' ' + self.name

    def change_parent(self, new_parent):
        self.parent = new_parent

    def add_child(self, item):
        self.children.append(item)

    def change_item_type(self, new_item_type):
        self.item_type = new_item_type

    def toggle_check(self):
        self.is_checked = not self.is_checked
