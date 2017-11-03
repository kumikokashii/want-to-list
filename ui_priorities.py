
from tkinter import *
from tkinter import ttk

from ui_tab_in_notebook import *

class UIPriorities(UITabInNB):
    def __init__(self, parent, tab_name, priority_list):
        super().__init__(parent, tab_name)
        self.priority_list = priority_list

    def refresh(self):
        table = []
        header = ['Name', 'Importance', 'Remove']
        table.append(header)

        for priority in self.priority_list:
            name = priority.name
            importance = priority.importance
            table.append([name, importance, 'X'])

        for i in range(len(table)):
            for j in range(len(table[i])):
                cell = Label(self, text=table[i][j])
                cell.grid(row=i, column=j)
