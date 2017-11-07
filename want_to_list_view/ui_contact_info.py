
from tkinter import *
from tkinter import ttk

from str_vars import *
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
        frame = self.view
        frame.cleanup()

        header = []
        for field in [name_, phone_, address_, 'Remove']:
            header.append(Label(frame, text=field))

        contact_infos = []
        for contact_info in self.contact_info_book:
            id = contact_info.id
            name = contact_info.name
            phone = contact_info.phone
            address = contact_info.address

            contact_info = []
            for text in [name, phone, address]:
                contact_info.append(Label(frame, text=text))
            x_button = Button(frame, text=remove_str_, command=(lambda id=id: self.controller.remove(id)))
            contact_info.append(x_button)
            contact_infos.append(contact_info)

        table = [header] + contact_infos

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

    def refresh_add(self):
        frame = self.add
        frame.cleanup()

        label = self.get_label_dict(frame, [name_, phone_, phone_exp_, address_,
                                            street_address_, city_, state_, zip_code_])
        form_dict = {}
        for field in [name_, phone_, street_address_, city_, state_, zip_code_]:
            form_dict[field] = Entry(frame)

        button = Button(self.add, text='Add ^_^', 
                        command=(lambda form_dict=form_dict:
                                 self.controller.add(self.get_add_values(form_dict))))

        table = [[label[name_], form_dict[name_]],
                 [label[phone_], form_dict[phone_], label[phone_exp_]],
                 [label[address_], form_dict[street_address_], label[street_address_]],
                 [None, form_dict[city_], label[city_]],
                 [None, form_dict[state_], label[state_]],
                 [None, form_dict[zip_code_], label[zip_code_]],
                 [None, button]]

        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] is None:
                    continue
                table[i][j].grid(row=i, column=j, sticky=W)

    def get_add_values(self, form_dict):
        values = {}
        for field, entry in form_dict.items():
            values[field] = entry.get()
        return values



