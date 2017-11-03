
from tkinter import *
from tkinter import ttk

from ui_tab_in_notebook import *

class UIItemList(UITabInNB):
    def __init__(self, parent, tab_name, item_list):
        super().__init__(parent, tab_name)
        self.item_list = item_list
        self.nb = ttk.Notebook(self)
        self.nb.grid()  # Need to specify parameters???
        self.view = UITabInNB(parent=self.nb, tab_name='View') 
        self.add = UITabInNB(parent=self.nb, tab_name='Add')

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

