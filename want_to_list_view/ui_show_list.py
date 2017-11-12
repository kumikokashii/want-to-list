from tkinter import *
from tkinter import *

from str_vars import *
from .ui_tab_in_notebook import *

import datetime

class UIShowList(UIFrame):
    def __init__(self, ui_item_list):
        super().__init__(ui_item_list)
        self.ui_item_list = ui_item_list
        self.controller = ui_item_list.controller
        self.current_list = ui_item_list.item_list.root
        self.show = ui_item_list.show 
        self.sort_key = name_

    def refresh(self, new_list=None):
        if new_list is not None:
            self.current_list = new_list
        self.cleanup() 

        sorted = self.get_sorted()
        parts = self.get_parts(sorted)
        self.make_grid(parts)

    def get_sorted(self):
        if self.show == 'current list only':
            sorted = self.current_list.get_sorted_with_label_text_by(self.sort_key)
        if self.show == 'all under this list':
            sorted = self.current_list.get_all_childless_items().get_sorted_with_label_text_by(self.sort_key)
        return sorted

    def show_onchange(self, show_var):
        self.ui_item_list.show = show_var.get()
        self.refresh()
        self.ui_item_list.refresh_item(self.current_list)

    def sort_by_onchange(self, sort_by_var):
        self.sort_key = sort_by_var.get()
        self.refresh()

    def get_parts(self, sorted):
        item = self.current_list
        parts = {}

        # Show
        label = ttk.Label(self, text='show')

        variable = StringVar(self)
        variable.set(self.show)
        variable.trace('w', lambda _0, _1, _2, show_var=variable: self.show_onchange(show_var))

        options = ['current list only', 'all under this list']
        option_menu = OptionMenu(self, variable, *options)
        parts['show'] = [label, option_menu]

        # Sort by
        label = ttk.Label(self, text='sort by')

        variable = StringVar(self)
        variable.set(self.sort_key)
        variable.trace('w', lambda _0, _1, _2, sort_by_var=variable: self.sort_by_onchange(sort_by_var))

        options = [name_, due_date_, priority_, created_date_]
        option_menu = OptionMenu(self, variable, *options)
        parts['sort'] = [label, option_menu]

        # Up button and List name
        if item.id != 0:  # If not top level
            parent_id = item.parent.id
            up_button = Button(self, text='^')
            up_button.bind('<Button-1>', lambda event, id=parent_id: self.controller.onclick_item(id))

            label = ttk.Label(self, text=item.name)
            label.bind('<Button-1>', lambda event, id=item.id: self.controller.onclick_title(id))
            parts['list name'] = [up_button, label]

        # List block
        list_block = []

        for group, items in sorted:
            if group is not None:  # Create label
                if isinstance(group, datetime.date):  # Format date
                    group = '{:%a, %b %-d, %Y}'.format(group)
                label = ttk.Label(self, text=group)
            group_label = None if (group is None) else label

            group_items = []
            for item in items:
                # Check button
                check_button = Checkbutton(self)
                if item.is_checked:
                    check_button_select()
                check_button.bind('<Button-1>', lambda event, id=item.id: self.controller.toggle_check(id))

                # Item name
                name = self.get_item_name(item, self.show)
                item_label = ttk.Label(self, text=name)
                item_label.bind('<Button-1>', lambda event, id=item.id: self.controller.onclick_item(id))

                group_items.append((check_button, item_label))

            list_block.append((group_label, group_items))

        parts['list block'] = list_block

        # Add new item
        add_button = Button(self, text='+')
        entry = Entry(self)
        add_button.bind('<Button-1>', lambda event, entry=entry: self.controller.add_item(entry.get(), item))
        parts['add'] = [add_button, entry]

        return parts

    def make_grid(self, parts):
        row_order = ['show', 'sort', 'list name', 'list block', 'add']

        current_row = 1
        for row_name in row_order:
            if row_name not in parts:
                continue

            # Options
            if row_name in ['show', 'sort']:
                label, option = parts[row_name]
                label['style'] = 'options.TLabel'
                label.grid(row=current_row, column=1, sticky=W+E, padx=2, pady=1)
                option.grid(row=current_row, column=2, sticky=W+E, padx=2, pady=1)

            # Up & List name
            if row_name == 'list name':
                button, label = parts[row_name]
                label['style'] = 'field.TLabel'
                button.grid(row=current_row, column=1, sticky=W+E, padx=2, pady=1)
                label.grid(row=current_row, column=2, sticky=W+E, padx=2, pady=1)

            # Items
            item_count = 1
            if row_name == 'list block':
                for group_label, items in parts[row_name]:
                    if group_label is not None:
                        group_label['style'] = 'sort_label.TLabel'
                        group_label.grid(row=current_row, column=1, columnspan=2, sticky=W+E, padx=2, pady=1)
                        current_row += 1

                    for check, label in items:
                        style = 'yellow_alt_1.TLabel' if (item_count % 2 == 1) else 'yellow_alt_2.TLabel'
                        label['style'] = style
                        check.grid(row=current_row, column=1, sticky=W+E, padx=2, pady=1)
                        label.grid(row=current_row, column=2, sticky=W+E, padx=2, pady=1)
                        current_row += 1
                        item_count += 1

                current_row -= 1  # Subtract last extra

            # Add
            if row_name == 'add':
                button, entered = parts[row_name]
                button.grid(row=current_row, column=1, sticky=W+E, padx=2, pady=1)
                entered.grid(row=current_row, column=2, sticky=W+E, padx=2, pady=1)

            current_row += 1
