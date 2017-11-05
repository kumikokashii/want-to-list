
from tkinter import *
from tkinter import ttk

from .ui_tab_in_notebook import *

class UIItemList(UITabInNB):
    def __init__(self, parent, tab_name, item_list):
        super().__init__(parent, tab_name)
        self.item_list = item_list
        self.left = UIFrame(self)
        self.left.grid(row=0, column=0)
        self.right = UIFrame(self)
        self.right.grid(row=0, column=1)
        self.current_list = item_list.root
        self.current_item = item_list.root
        self.sort_key = 'name'

    def refresh_left(self):
        frame = self.left
        frame.cleanup() 

        table = []

        # List name
        if self.current_list.id != 0:  # If not top level
            parent_id = self.current_list.parent.id
            label_1 = Label(frame, text='^')
            label_1.bind('<Button-1>', lambda event, id=parent_id: self.controller.onclick_item(id))

            label_2 = Label(frame, text=self.current_list.name)
            label_2.bind('<Button-1>', lambda event, id=self.current_list.id: self.controller.onclick_title(id))
            table.append([label_1, label_2])

        # Items
        sorted = self.current_list.get_sorted_by(self.sort_key)
        for item in sorted:
            id = item.id
            is_checked = item.is_checked
            name = item.name

            check_button = Checkbutton(frame)
            if is_checked:
                check_button.select()
            check_button.bind('<Button-1>', lambda event, id=id: self.controller.toggle_check(id))

            label = Label(frame, text=name)
            label.bind('<Button-1>', lambda event, id=id: self.controller.onclick_item(id))

            table.append([check_button, label])

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

    def refresh_right(self):
        frame = self.right
        frame.cleanup()

        if self.current_item.id == 0:  # If top level
            return

        item = self.current_item
        item_dict = {'Due': item.due_date,
                     'Priority': item.priority,
                     'Img': item.picture,
                     'Money': item.money,
                     'Contact Info': item.contact_info,
                     'Created on': item.created_date} 
        format_dict = {'Due': (lambda due_date: '{:%a, %b %-d, %Y}'.format(due_date)),
                       'Priority': (lambda priority: priority.name),
                       'Money': (lambda money: str(money)),
                       'Contact Info': (lambda contact_info: str(contact_info)),
                       'Created on': (lambda created_date: '{:%-m/%-d/%Y %-I:%M%p}'.format(created_date))}

        table = []

        # Name
        label = Label(self.right, text=item.name)
        table.append([label])

        # Details
        for field in ['Due', 'Priority', 'Img', 'Money', 'Contact Info', 'Created on']:
            content = item_dict[field]
            if content is None:
                continue

            format = format_dict[field]
            value = format(content)
            label_1 = Label(frame, text=field)
            label_2 = Label(frame, text=value)
            table.append([label_1, label_2])

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

