
class Item():
    def __init__(self, id, name, item_type, parent_item,
                 created_date, due_date, priority, picture, 
                 money, contact_info):
        self.id = id  # int
        self.name = name  # str
        self.item_type = item_type  # ItemType
        self.parent_item = parent_item  # Item
        self.is_checked = False  # boolean
        self.created_date = created_date  # date
        self.due_date = due_date  # date
        self.priority = priority  # Priority
        self.picture = picture  # Picture
        self.money = money  # Money
        self.contact_info = contact_info  # ContactInfo

    def __str__(self):
        attribute_names = ['ID', 'Name', 'Type', 'Parent Item', 'Checked', 
                           'Created Date', 'Due Date', 'Prority', 'Picture', 
                           'Money', 'Contact Info']
        attribute_vars = [self.id, self.name, self.item_type, self.parent_item, self.is_checked, 
                          self.created_date, self.due_date, self.priority, self.picture, 
                          self.money, self.contact_info]
        output = ''
        for i in range(len(attribute_names)):
            output += attribute_names[i] + ': '
            if attribute_vars[i] is not None:
                if attribute_names[i] == 'Parent Item':
                    output += attribute_vars[i].short_str()
                else:
                    output += str(attribute_vars[i])
            else:
                output += 'None'
            output += '\n'
        return output

    def short_str(self):
        return str(self.id) + ' ' + self.name
