
from tkinter import *
from tkinter import ttk

class UIItemList():
    def __init__(self, item_list, nb=None, tabs=None):
        self.item_list = item_list
        self.nb = nb
        self.view = None if tabs is None else tabs['View']
        self.add = None if tabs is None else tabs['Add']

    def set_attributes(self, nb, view, add):
        self.nb = nb
        self.view = view
        self.add = add

    def refresh_view(self):
        table = []
        header = ['Check', 'Name', 'Due Date', 'Priority']
        table.append(header)

        for item in self.item_list:
            is_checked = item.is_checked
            name = item.name
            due_date = item.due_date
            priority = item.priority
            table.append([is_checked, name, due_date, priority])

        for i in range(len(table)):
            for j in range(len(table[i])):
                cell = Label(self.view, text=table[i][j])
                cell.grid(row=i, column=j)

