from .money import *

from str_vars import *

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

    def __eq__(self, other):  # for ==
        return self.id == other.id

    def short_str(self):
        return str(self.id) + ' ' + self.name

    def get_sorted_by_due_date(self):
        self.sort(key=lambda item: item.id)
        not_none_list = []
        none_list = []
        for item in self:
            if item.due_date is None:
                none_list.append(item)
            else:
                not_none_list.append(item)
        not_none_list.sort(key=lambda item: item.due_date, reverse=True)
        return not_none_list + none_list

    def get_sorted_by_priority(self):
        self.sort(key=lambda item: item.id)
        not_none_list = []
        none_list = []
        for item in self:
            if item.priority is None:
                none_list.append(item)
            else:
                not_none_list.append(item)
        not_none_list.sort(key=lambda item: item.priority.importance)
        return not_none_list + none_list

    def get_sorted_by(self, key):
        if key == name_:
            return sorted(self, key=lambda item: item.name)  # name is never None
        if key == due_date_:
            return self.get_sorted_by_due_date()
        if key == priority_:
            return self.get_sorted_by_priority()
        if key == created_date_:
            return sorted(self, key=lambda item: item.created_date)  # created_date is never None

    def update_name(self, name):
        self.name = name

    def update_due_date(self, due_date):
        self.due_date = due_date

    def update_priority(self, priority):
        self.priority = priority

    def refresh_money_amount_self_and_parents(self):
        if self.id == 0:  # Done if root
           return
        sum_amount = None
        for item in self:
            if item.money is None:
                continue
            if sum_amount is None:
                sum_amount = item.money.amount
            else:
                sum_amount += item.money.amount
        self.update_money_amount(sum_amount)
        self.parent.refresh_money_amount_self_and_parents()

    def update_money_amount(self, amount):
        # Update self
        if amount is None:
            self.money = None
            return

        if self.money is None:
            self.money = Money(amount)
        else:
            self.money.amount = amount

        # Update parent, its parent, etc.
        self.parent.refresh_money_amount_self_and_parents()

    def update_contact_info(self, contact_info):
        self.contact_info = contact_info

    def toggle_check(self):
        self.is_checked = not self.is_checked

