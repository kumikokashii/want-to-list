from item_type import *

class ItemTypeList():
    def __init__(self):
        self.list = []

    def __str__(self):
        output = ''
        for item_type in self.list:
            output += str(item_type)
            output += '\n'
        return output

    def add(self, item_type):
        self.list.append(item_type)

    def get_item_type_by_name(self, name):
        for item_type in self.list:
            if item_type.name == name:
                return item_type
        return None

    def set_default(self):
        self.list = []
        self.add(ItemType(0, 'check'))
        self.add(ItemType(1, 'note'))

