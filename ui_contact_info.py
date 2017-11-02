
from tkinter import *
from tkinter import ttk

class UIContactInfo():
    def __init__(self, contact_info_book, nb=None, tabs=None):
        self.contact_info_book = contact_info_book
        self.nb = nb
        self.view = None if tabs is None else tabs['View']
        self.add = None if tabs is None else tabs['Add']

    def set_attributes(self, nb, view, add):
        self.nb = nb
        self.view = view
        self.add = add

    def refresh_view(self):
        table = []
        header = ['Name', 'Phone', 'Address']
        table.append(header)

        for contact_info in self.contact_info_book.book:
            name = contact_info.name
            phone = contact_info.phone
            address = contact_info.address
            table.append([name, phone, address])

        for i in range(len(table)):
            for j in range(len(table[i])):
                cell = Label(self.view, text=table[i][j])
                cell.grid(row=i, column=j)

