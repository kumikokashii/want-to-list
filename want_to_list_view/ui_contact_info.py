
from tkinter import *
from tkinter import ttk

from .ui_tab_in_notebook import *

class UIContactInfo(UITabInNB):
    def __init__(self, parent, tab_name, contact_info_book):
        super().__init__(parent, tab_name)
        self.contact_info_book = contact_info_book

        self.nb = ttk.Notebook(self)
        self.nb.grid()  # Need to specify parameters???
        self.view = UITabInNB(parent=self.nb, tab_name='View')
        self.add = UITabInNB(parent=self.nb, tab_name='Add')

    def refresh_view(self):
        self.view.cleanup()

        table = []

        row = []
        for header in ['Name', 'Phone', 'Address', 'Remove']:
            row.append(Label(self.view, text=header)) 
        table.append(row)

        for contact_info in self.contact_info_book:
            id = contact_info.id
            name = contact_info.name
            phone = contact_info.phone
            address = contact_info.address

            row = []
            for cell in [name, phone, address]:
                row.append(Label(self.view, text=cell))
            remove_by_id = self.controller.get_remove_by_id_func(id)
            x_button = Button(self.view, text='X', command=remove_by_id)
            row.append(x_button)
            table.append(row)

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

    def initialize_add(self):
        table = [['Name', -1, None], 
                 ['Phone', -1, '10 digits'], 
                 ['Address', -1, 'Street Address'], 
                 [None, -1, 'City'], 
                 [None, -1, 'State'], 
                 [None, -1, 'Zip Code']]

        fields = ['name', 'phone', 'street address', 'city', 'state', 'zip code']
        inputs = []
        for i in range(len(table)):
            for j in range(len(table[i])):
                elem = table[i][j]
                if elem is None:
                    continue
                if elem == -1:
                    cell = Entry(self.add)
                    inputs.append(cell)
                else:    
                    cell = Label(self.add, text=elem)
                cell.grid(row=i, column=j)

        entries = {}
        for i in range(len(fields)):
            field = fields[i]
            input = inputs[i]
            entries[field] = input

        button = Button(self.add, text='Add ^_^', command=(lambda: self.controller.add(entries)))
        button.grid(row=len(table), column=1)
