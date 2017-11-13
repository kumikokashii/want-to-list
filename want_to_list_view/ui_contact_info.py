
from tkinter import *
from tkinter import ttk

from str_vars import *
from .ui_tab_in_notebook import *

class UIContactInfo(UITabInNB):
    def __init__(self, parent, tab_name, contact_info_book):
        super().__init__(parent, tab_name)
        self.contact_info_book = contact_info_book

        self.nb = ttk.Notebook(self)
        self.nb.grid()
        self.view = UITabInNB(parent=self.nb, tab_name='View')
        self.add = UITabInNB(parent=self.nb, tab_name='Add')

    def refresh_view(self):
        self.view.cleanup()

        parts = self.get_view_parts()
        self.make_view_grid(parts)

    def get_view_parts(self):
        frame = self.view

        parts = {}

        # Header
        header = []
        for field in [name_, phone_, address_, 'Remove']:
            header.append(ttk.Label(frame, text=field))
        parts['header'] = header

        # Contact Infos
        contact_infos = []
        sorted = self.contact_info_book.get_sorted_by_name()
        for contact_info in sorted:
            id = contact_info.id
            name = contact_info.name
            phone = contact_info.phone
            address = contact_info.address

            contact_info = []
            for text in [name, phone, address]:
                contact_info.append(ttk.Label(frame, text=text))
            x_button = Button(frame, text=remove_str_, command=(lambda id=id: self.controller.remove(id)))
            contact_info.append(x_button)

            contact_infos.append(contact_info)
        parts['content'] = contact_infos

        return parts

    def make_view_grid(self, parts):
        # Header
        for i in range(len(parts['header'])):
            w = parts['header'][i]
            w['style'] = 'field.TLabel'  # Color
            w.grid(row=1, column=i+1, sticky=W+E, padx=2, pady=1)

        # Contact Infos
        for i in range(len(parts['content'])):
            ith_row = parts['content'][i]
            for j in range(len(ith_row)):
                w = ith_row[j]

                # Color if not remove button
                style = 'grey_alt_1.TLabel' if (i % 2 == 1) else 'grey_alt_2.TLabel'
                if w.winfo_class() == 'TLabel':
                    w['style'] = style 
                
                w.grid(row=i+2, column=j+1, sticky=W+E, padx=2, pady=1)

    def refresh_add(self):
        self.add.cleanup()
        parts = self.get_add_parts()
        self.make_add_grid(parts)

    def get_add_parts(self):
        # parts is made of 4 pieces: label, sub label, form, button

        # Label and sub label
        label_dict = self.get_label_dict(self.add, [name_, phone_, address_])
        sub_label_dict = self.get_label_dict(self.add, [phone_exp_, street_address_, city_, state_, zip_code_])

        # Form
        form_dict = {}
        for field in [name_, phone_, street_address_, city_, state_, zip_code_]:
            form_dict[field] = Entry(self.add)

        # Button
        button = Button(self.add, text='Add ^_^', 
                        command=(lambda form_dict=form_dict:
                                 self.controller.add(self.get_add_values(form_dict))))

        parts = {'label': label_dict, 'sub label': sub_label_dict,
                 'form': form_dict, 'button': button}
        return parts

    def make_add_grid(self, parts):
        # Label
        current_row = 1
        label_order = [name_, phone_, address_]
        for label_name in label_order:
            label = parts['label'][label_name]
            label['style'] = 'field.TLabel'
            label.grid(row=current_row, column=1, sticky=W+E, padx=2, pady=1)
            current_row += 1

        # Sub label
        current_row = 2
        sub_label_order = [phone_exp_, street_address_, city_, state_, zip_code_]
        for sub_label_name in sub_label_order:
            sub_label = parts['sub label'][sub_label_name]
            sub_label['style'] = 'grey_alt_1.TLabel' if (current_row % 2 == 1) else 'grey_alt_2.TLabel'
            sub_label.grid(row=current_row, column=3, sticky=W+E, padx=2, pady=1)
            current_row += 1

        # Form
        current_row = 1
        form_order = [name_, phone_, street_address_, city_, state_, zip_code_]
        for form_name in form_order:
            form = parts['form'][form_name]
            form.grid(row=current_row, column=2, sticky=W+E, padx=2, pady=1)
            current_row += 1

        # Add button
        button = parts['button']
        button.grid(row=7, column=2, sticky=W+E, padx=2, pady=1)

    def get_add_values(self, form_dict):
        values = {}
        for field, content in form_dict.items():
            values[field] = content.get()
        return values



