from tkinter import *
from tkinter import *

from str_vars import *
from .ui_tab_in_notebook import *

class UIShowItem(UIFrame):
    def __init__(self, ui_item_list):
        super().__init__(ui_item_list)
        self.ui_item_list = ui_item_list
        self.current_item = ui_item_list.item_list.root

    def refresh(self, new_item=None):
        if new_item is not None:
            self.current_item = new_item
        self.cleanup() 

        if self.current_item.id == 0:  # If top level
            return

        parts = self.get_parts()
        self.make_grid(parts)

    def get_format_dict(self):
        format_dict = {due_date_: (lambda due_date: '{:%a, %b %-d, %Y}'.format(due_date)),
                       priority_: (lambda priority: priority.name),
                       picture_: (lambda picture: self.get_resized_tk_image(picture, 200)),
                       money_: (lambda money: str(money)),
                       contact_info_: (lambda contact_info: contact_info.block_str()),
                       created_date_: (lambda created_date: '{:%-m/%-d/%Y %-I:%M%p}'.format(created_date))}
        return format_dict

    def get_parts(self):
        item = self.current_item
        item_dict = self.get_item_dict(item)

        parts = {}

        # Name
        name = self.get_item_name(item, self.ui_item_list.show)
        parts[name_] = ttk.Label(self, text=name)

        # Details
        format_dict = self.get_format_dict()
        for field in [due_date_, priority_, picture_, money_, contact_info_, created_date_]:
            content = item_dict[field]
            if content is None:
                continue

            format = format_dict[field]
            value = format(content)
            label_1 = ttk.Label(self, text=field)
            if field == picture_:
                label_2 = ttk.Label(self, image=value)
                label_2.image = value
            else:
                label_2 = ttk.Label(self, text=value)
            parts[field] = [label_1, label_2]

        # Edit button
        edit_button = Button(self, text='Edit me')
        edit_button.bind('<Button-1>', lambda event, item=item: self.ui_item_list.edit_item_mode(item))
        parts['edit'] = edit_button

        # Add new item
        if len(item) == 0:  # If has no item
            add_button = Button(self, text='+')
            entry = Entry(self)
            add_button.bind('<Button-1>', lambda event, entry=entry: self.controller.add_child(entry.get(), item))
            parts['add'] = [add_button, entry]

        return parts

    def make_grid(self, parts):
        row_order = [name_, due_date_, priority_, picture_, money_,
                     contact_info_, created_date_, 'edit', 'add']

        current_row = 1
        for row_name in row_order:
            if row_name not in parts:
                continue

            # Item name
            if row_name == name_:
                label = parts[row_name]
                label['style'] = 'subfield.TLabel'
                label.grid(row=current_row, column=1, columnspan=2, sticky=W+E, padx=2, pady=1)

            # Details
            if row_name not in [name_, 'edit', 'add']:
                label_1, label_2 = parts[row_name]

                # Color
                style = 'grey_alt_1.TLabel' if (current_row % 2 == 1) else 'grey_alt_2.TLabel'
                label_1['style'] = style
                if row_name != picture_:
                    label_2['style'] = style

                label_1.grid(row=current_row, column=1, sticky=W+E+N+S, padx=2, pady=1)
                label_2.grid(row=current_row, column=2, sticky=W+E+N+S, padx=2, pady=1)

            # Edit button
            if row_name == 'edit':
                button = parts[row_name]
                button.grid(row=current_row, column=1, columnspan=2, sticky=W+E, padx=2, pady=1)

            # Add
            if row_name == 'add':
                button, entered = parts[row_name]
                button.grid(row=current_row, column=1, sticky=W+E, padx=2, pady=1)
                entered.grid(row=current_row, column=2, sticky=W+E, padx=2, pady=1)

            current_row += 1

