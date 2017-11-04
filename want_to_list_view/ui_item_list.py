
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
        self.current_item = None
        self.sort_key = 'name'

    def refresh_left(self):
        self.left.cleanup() 

        table = []

        row = []
        for header in ['Check', 'Name', 'Due Date', 'Priority']:
            row.append(Label(self.left, text=header))
        table.append(row)

        sorted = self.current_list.get_sorted_by(self.sort_key)
        for item in sorted:
            id = item.id
            is_checked = item.is_checked
            name = item.name
            due_date = item.due_date
            priority = item.priority

            row = []

            check_button = Checkbutton(self.left)
            if is_checked:
                check_button.select()
            check_button.bind('<Button-1>', lambda event, id=id: self.controller.toggle_check(id))
            row.append(check_button)

            for cell in [name, due_date, priority]:
                label = Label(self.left, text=cell)
                label.bind('<Button-1>', lambda event, id=id: self.controller.onclick_item(id))
                row.append(label)

            table.append(row)

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

    def refresh_right(self):
        self.right.cleanup()

        item = self.current_item
        name = item.name
        created_date = item.created_date
        due_date = item.due_date
        priority = item.priority
        picture = item.picture
        money = item.money
        contact_info = item.contact_info

        table = []

        # Name
        label = Label(self.right, text=name)
        table.append([label])

        # Due Date
        label_1 = Label(self.right, text='Due')
        label_2 = Label(self.right, text=due_date)
        table.append([label_1, label_2])

        # Priority
        label = Label(self.right, text=priority)
        table.append([label])

        # Picture
        label_1 = Label(self.right, text='Img')
        label_2 = Label(self.right, text=picture)
        table.append([label_1, label_2])

        # Money
        label_1 = Label(self.right, text='Money')
        label_2 = Label(self.right, text=money)
        table.append([label_1, label_2])
        
        # Contact Info
        label_1 = Label(self.right, text='Contact Info')
        label_2 = Label(self.right, text=contact_info)
        table.append([label_1, label_2])

        # Created Date
        label_1 = Label(self.right, text='Created on')
        label_2 = Label(self.right, text=created_date)
        table.append([label_1, label_2])

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

