
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

        pieces = self.get_pieces()
        form_dict = self.get_form_dict(pieces)
        self.add_button_to_pieces(pieces, form_dict)

        parts = self.get_parts(pieces)
        self.make_grid(parts)

    def get_pieces(self):
        pieces = {}

        # Header
        header = []
        for field in ['Name', 'Importance', 'Remove']:
            header.append(ttk.Label(self, text=field))
        pieces['header'] = header

        # Existing priorities
        existing = []
        sorted = self.priority_list.get_sorted_by_importance()
        for priority in sorted:
            entry_1 = Entry(self)
            entry_1.insert(0, priority.name)
            entry_2 = Entry(self, width=3)
            entry_2.insert(0, priority.importance)
            x_button = Button(self, text=remove_str_,
                              command=(lambda id=priority.id: self.controller.remove(id)))
            existing.append((priority.id, entry_1, entry_2, x_button))
        pieces['existing'] = existing

        # New priority
        entry_1 = Entry(self, width=3)
        entry_2 = Entry(self, width=3)
        pieces['new'] = (-1, entry_1, entry_2)  # Id = -1 indicates it doesn't currently exist

        return pieces 

    def get_form_dict(self, pieces):
        form_dict = {}

        # Existing priorities
        for id, entry_1, entry_2, x_button in pieces['existing']:
            form_dict[id] = (entry_1, entry_2)

        # New priority
        id, entry_1, entry_2 = pieces['new']
        form_dict[id] = (entry_1, entry_2)

        return form_dict

    def add_button_to_pieces(self, pieces, form_dict):
        button = Button(self, text='Edit!', 
                        command=(lambda: self.controller.edit(self.get_values(form_dict))))
        pieces['edit'] = button

    def get_parts(self, pieces):
        parts = {}

        for field, content in pieces.items():
            if field == 'existing':
                parts[field] = []
                for sub_content in content:
                   parts[field].append(sub_content[1:])
            elif field == 'new':
                parts[field] = content[1:]
            else:
                parts[field] = content 

        return parts

    def make_grid(self, parts):
        # Header
        for i in range(len(parts['header'])):
            w = parts['header'][i]
            w['style'] = 'field.TLabel'  # Color
            w.grid(row=1, column=i+1, sticky=W+E, padx=2, pady=1)

        # Existing priorities
        for i in range(len(parts['existing'])):
            ith_row = parts['existing'][i]
            for j in range(len(ith_row)):
                w = ith_row[j]
                w.grid(row=i+2, column=j+1, sticky=W+E, padx=2, pady=1)
        current_row = 1 + len(parts['existing']) + 1

        # New priority
        for i in range(len(parts['new'])):
            w = parts['new'][i]
            w.grid(row=current_row, column=i+1, sticky=W+E, padx=2, pady=1)
        current_row += 1

        # Edit button
        button = parts['edit']
        button.grid(row=current_row, column=1, columnspan=2, sticky=W+E, padx=2, pady=1)

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


