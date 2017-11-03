
from tkinter import *
from tkinter import ttk

from .ui_tab_in_notebook import *

class UIPriorities(UITabInNB):
    def __init__(self, parent, tab_name, priority_list):
        super().__init__(parent, tab_name)
        self.priority_list = priority_list

    def refresh(self):
        self.cleanup()

        table = []

        row = []
        for header in ['Name', 'Importance', 'Remove']:
            row.append(Label(self, text=header)) 
        table.append(row)

        entries = {}

        sorted = self.priority_list.get_sorted_by_importance()
        for priority in sorted:
            id = priority.id
            name = priority.name
            importance = priority.importance

            row = []
            for cell in [name, importance]:
                entry = Entry(self)
                entry.insert(0, cell)
                row.append(entry)
            entries[id] = row
            row.append(Button(self, text='X', command=(lambda: self.controller.remove(id))))
            table.append(row)

        row = []
        for i in range(2):
            row.append(Entry(self))
        entries[-1] = row
        table.append(row)

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

        button = Button(self, text='Edit!', command=(lambda: self.controller.edit(entries)))
        button.grid()

