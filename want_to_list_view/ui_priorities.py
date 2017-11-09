
from tkinter import *
from tkinter import ttk

from str_vars import *
from .ui_tab_in_notebook import *

class UIPriorities(UITabInNB):
    def __init__(self, parent, tab_name, priority_list):
        super().__init__(parent, tab_name)
        self.priority_list = priority_list

    def refresh(self):
        self.cleanup()

        header = ['Name', 'Importance', 'Remove']
        label = self.get_label_dict(self, header)
        header_label = [label[h] for h in header]

        sorted = self.priority_list.get_sorted_by_importance()
        n = len(sorted)

        all_p = []
        for i in range(n+1):
            priority = (None if i == n else sorted[i])
            id = (-1 if i == n else priority.id)
            name = ('' if i == n else priority.name)
            importance = ('' if i == n else priority.importance)

            entry_1 = Entry(self)
            entry_1.insert(0, name)
            entry_2 = Entry(self)
            entry_2.insert(0, importance)
            x_button = Button(self, text=remove_str_, 
                              command=(lambda id=id: self.controller.remove(id)))
            if i == n:
                x_button = None
            all_p.append((id, entry_1, entry_2, x_button))

        form_dict = {}
        for i in range(len(all_p)):
            id, entry_1, entry_2 = all_p[i][0: 3]
            form_dict[id] = (entry_1, entry_2)

        button = Button(self, text='Edit!', 
                        command=(lambda: self.controller.edit(self.get_values(form_dict))))

        table = [header_label] + [[p[1], p[2], p[3]] for p in all_p] + [[button]]

        for i in range(len(table)):
            for j in range(len(table[i])):
                w = table[i][j]
                if w is None:
                    continue
                w_class = w.winfo_class()
                if i == 0:
                    w['style'] = 'field.' + w_class
                w.grid(row=i, column=j, sticky=W+E, padx=2, pady=1)

    def get_values(self, form_dict):
        values = []

        for id in form_dict:
            entry_1, entry_2 = form_dict[id]
            name = entry_1.get()
            importance = entry_2.get()
            if id == -1:  # New priority row
                if (name == '') or (importance == ''):
                    continue
                else:
                    id = self.priority_list.get_next_id()
            values.append((id, name, importance))
        return values


