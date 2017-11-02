from tkinter import *
from tkinter import ttk

from ui_list import *
from ui_contact_info import *

class UserInterface(Tk):
    def __init__(self, organizer):
        super().__init__()
        self.list = UIList(organizer.list)  
        self.contact_info = UIContactInfo(organizer.contact_info_book)

    def add_notebook(self, tab_names, parent=None):
        if parent is None:
            nb = ttk.Notebook(self)
        else:
            nb = ttk.Notebook(parent)
        nb.grid()  # Need to specify parameters???

        tabs = {}
        for tab_name in tab_names:
            tab = ttk.Frame(nb)
            nb.add(tab, text=tab_name)
            tabs[tab_name] = tab
        return nb, tabs

    def initialize(self):
        self.title('Want To List')
        self.geometry('800x500')

        # Add tabs
        self.nb, self.tabs = self.add_notebook(['List', 'Contact Info', 'Priorities'])
        
        # Add tabs within tabs
        nb, tabs = self.add_notebook(['View', 'Add'], self.tabs['List'])
        self.list.set_attributes(nb=nb, view=tabs['View'], add=tabs['Add'])
        self.list.refresh_view()

        nb, tabs = self.add_notebook(['View', 'Add'], self.tabs['Contact Info'])
        self.contact_info.set_attributes(nb=nb, view=tabs['View'], add=tabs['Add'])
        self.contact_info.refresh_view()

        # Start
        self.mainloop()

