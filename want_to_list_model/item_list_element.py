
class ItemListElement(list):
    def __init__(self, id, name, item_type, parent,
                 created_date, due_date, priority, picture,
                 money, contact_info, is_checked=False):
        super().__init__()
        self.id = id  # int
        self.name = name  # str
        self.item_type = item_type  # ItemType
        self.parent = parent  # ItemList
        self.created_date = created_date  # datetime
        self.due_date = due_date  # date
        self.priority = priority  # Priority
        self.picture = picture  # Picture
        self.money = money  # Money
        self.contact_info = contact_info  # ContactInfo
        self.is_checked = is_checked  # boolean

    def __str__(self):
        attribute_names = ['ID', 'Name', 'Type', 'Parent', 'Items', 
                           'Created Date', 'Due Date', 'Prority', 'Picture',
                           'Money', 'Contact Info', 'Checked']
        attribute_vars = [self.id, self.name, self.item_type, self.parent, self,
                          self.created_date, self.due_date, self.priority, self.picture,
                          self.money, self.contact_info, self.is_checked]
        output = ''
        for i in range(len(attribute_names)):
            a_name = attribute_names[i]
            a_var = attribute_vars[i]

            output += a_name + ': '
            if a_var is None:
                output += 'None'
            elif a_name == 'Parent':
                output += a_var.short_str()
            elif a_name == 'Items':
                items_output = []
                for item in a_var:
                    items_output.append(item.short_str())
                output += ', '.join(items_output)
            else:
                output += str(a_var)
            output += '\n'
        return output

    def short_str(self):
        return str(self.id) + ' ' + self.name

    def get_sorted_by(self, key):
        if key == 'name':
            return sorted(self, key=lambda item: item.name)
        if key == 'created date':
            return sorted(self, key=lambda item: item.created_date)
        if key == 'due date':
            return sorted(self, key=lambda item: item.due_date)
        if key == 'priority':
            return sorted(self, key=lambda item: item.priority)

    def change_item_type(self, new_item_type):
        self.item_type = new_item_type

    def change_parent(self, new_parent):
        self.parent = new_parent

    def toggle_check(self):
        self.is_checked = not self.is_checked

