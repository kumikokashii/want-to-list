
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

            name_importance_entries = []
            for cell in [name, importance]:
                entry = Entry(self)
                entry.insert(0, cell)
                name_importance_entries.append(entry)
            entries[id] = name_importance_entries
            remove_by_id = self.controller.get_remove_by_id_func(id)
            x_button = Button(self, text='X', command=remove_by_id)
            row = name_importance_entries + [x_button]
            table.append(row)

        name_importance_entries = []
        for i in range(2):
            entry = Entry(self)
            name_importance_entries.append(entry)
        entries[-1] = name_importance_entries
        table.append(name_importance_entries)

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

        button = Button(self, text='Edit!', command=(lambda: self.controller.edit(entries)))
        button.grid()

