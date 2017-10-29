from datetime import datetime

class Item():
    def __init__(self, name, item_type, parent_item_name, 
                 due_date, priority, picture, money, contact_info):
        self.name = name
        self.item_type = item_type
        self.parent_item_name = parent_item_name
        self.is_checked = False
        self.created_date = datetime.today().date()
        self.due_date = due_date
        self.priority = priority
        self.picture = picture
        self.money = money
        self.contact_info = contact_info
