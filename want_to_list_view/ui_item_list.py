
from tkinter import *
from tkinter import ttk

from str_vars import *
from .ui_tab_in_notebook import *

import datetime

class UIItemList(UITabInNB):
    def __init__(self, parent, tab_name, organizer): 
        super().__init__(parent, tab_name)
        self.item_list = organizer.item_list
        self.priority_list = organizer.priority_list
        self.contact_info_book = organizer.contact_info_book
        self.left = UIFrame(self)
        self.left.grid(row=0, column=0, sticky=N)
        self.right = UIFrame(self)
        self.right.grid(row=0, column=1, sticky=N)
        self.current_list = self.item_list.root
        self.current_item = self.item_list.root
        self.show = 'current list only'
        self.sort_key = name_

    def get_item_dict(self, item):
        item_dict = {name_: item.name,
                     due_date_: item.due_date,
                     priority_: item.priority,
                     picture_: item.picture,
                     money_: item.money,
                     contact_info_: item.contact_info,
                     created_date_: item.created_date}
        return item_dict

    def show_onchange(self, show_var):
        self.show = show_var.get()
        self.current_item = self.current_list
        self.refresh_left()
        self.refresh_right()

    def sort_by_onchange(self, sort_by_var):
        self.sort_key = sort_by_var.get()
        self.refresh_left()

    def get_items_table(self, frame, sorted):
        items_table = []

        for label_text, items in sorted:
            if label_text is not None:
                if isinstance(label_text, datetime.date):  # Format date
                    label_text = '{:%a, %b %-d, %Y}'.format(label_text)
                label = ttk.Label(frame, text=label_text)
                items_table.append([label])

            for item in items:
                item_row = self.get_item_row(frame, item)
                items_table.append(item_row)

        return items_table

    def get_item_name(self, item):
        name = item.name 
        if self.show == 'current list only':
            return name
        parent = item.parent
        if parent.id == 0:  # If top level
            return name
        return name + ' [' + parent.name + ']'

    def get_item_row(self, frame, item):
            id = item.id
            is_checked = item.is_checked
            name = self.get_item_name(item)

            check_button = Checkbutton(frame)
            if is_checked:
                check_button.select()
            check_button.bind('<Button-1>', lambda event, id=id: self.controller.toggle_check(id))

            label = ttk.Label(frame, text=name)
            label.bind('<Button-1>', lambda event, id=id: self.controller.onclick_item(id))

            return [check_button, label]

    def refresh_left(self, new_list=None):
        if new_list is not None:
            self.current_list = new_list
        frame = self.left
        frame.cleanup() 

        table = []

        # Show
        label = ttk.Label(frame, text='show')

        variable = StringVar(frame)
        variable.set(self.show)
        variable.trace('w', lambda _0, _1, _2, show_var=variable: self.show_onchange(show_var))

        options = ['current list only', 'all under this list']
        option_menu = OptionMenu(frame, variable, *options)
        table.append([label, option_menu])

        # Sort by
        label = ttk.Label(frame, text='sort by')

        variable = StringVar(frame)
        variable.set(self.sort_key)
        variable.trace('w', lambda _0, _1, _2, sort_by_var=variable: self.sort_by_onchange(sort_by_var))

        options = [name_, due_date_, priority_, created_date_]
        option_menu = OptionMenu(frame, variable, *options)
        table.append([label, option_menu])

        # List name
        if self.current_list.id != 0:  # If not top level
            parent_id = self.current_list.parent.id
            up_button = Button(frame, text='^')
            up_button.bind('<Button-1>', lambda event, id=parent_id: self.controller.onclick_item(id))

            label = ttk.Label(frame, text=self.current_list.name)
            label.bind('<Button-1>', lambda event, id=self.current_list.id: self.controller.onclick_title(id))
            table.append([up_button, label])

        # Items
        if self.show == 'current list only':
            sorted = self.current_list.get_sorted_with_label_text_by(self.sort_key)
        if self.show == 'all under this list':
            sorted = self.current_list.get_all_childless_items().get_sorted_with_label_text_by(self.sort_key)

        items_table = self.get_items_table(frame, sorted)
        table += items_table

        # Add new item
        add_button = Button(frame, text='+')
        entry = Entry(frame)
        add_button.bind('<Button-1>', lambda event, entry=entry: self.controller.add_item(entry.get(), self.current_list))
        table.append([add_button, entry])

        for i in range(len(table)):
            for j in range(len(table[i])):
                w = table[i][j]
                w_class = w.winfo_class()
                columnspan = 1
                if (i in [0, 1]) & (w_class == 'TLabel'):
                    w['style'] = 'options.' + w_class
                elif (j == 0) & (w_class == 'TLabel'):
                    w['style'] = 'sort_label.' + w_class
                    columnspan = 2
                elif (j == 1) & (w_class == 'TLabel'):
                    if (self.current_list.id != 0) & (i == 2): 
                        w['style'] = 'field.' + w_class
                    elif i % 2 == 1:
                        w['style'] = 'yellow_alt_1.' + w_class
                    else:
                        w['style'] = 'yellow_alt_2.' + w_class
                w.grid(row=i, column=j, columnspan=columnspan, sticky=W+E, padx=2, pady=1)

    def refresh_right(self, new_item=None):
        if new_item is not None:
            self.current_item = new_item
        frame = self.right
        frame.cleanup()

        if self.current_item.id == 0:  # If top level
            return

        item = self.current_item
        item_dict = self.get_item_dict(item)
        format_dict = {due_date_: (lambda due_date: '{:%a, %b %-d, %Y}'.format(due_date)),
                       priority_: (lambda priority: priority.name),
                       money_: (lambda money: str(money)),
                       contact_info_: (lambda contact_info: contact_info.block_str()),
                       created_date_: (lambda created_date: '{:%-m/%-d/%Y %-I:%M%p}'.format(created_date))}

        table = []

        # Name
        name = self.get_item_name(item)

        label = ttk.Label(frame, text=name)
        table.append([label])

        # Details
        for field in [due_date_, priority_, picture_, money_, contact_info_, created_date_]:
            content = item_dict[field]
            if content is None:
                continue

            format = format_dict[field]
            value = format(content)
            label_1 = ttk.Label(frame, text=field)
            label_2 = ttk.Label(frame, text=value)
            table.append([label_1, label_2])

        # Edit button
        edit_button = Button(frame, text='Edit me')
        edit_button.bind('<Button-1>', lambda event: self.to_edit_mode())
        table.append([edit_button])

        # Add new item
        if len(self.current_item) == 0:  # If has no item
            add_button = Button(frame, text='+')
            entry = Entry(frame)
            add_button.bind('<Button-1>', lambda event, entry=entry: self.controller.add_child(entry.get(), self.current_item))
            table.append([add_button, entry])

        for i in range(len(table)):
            for j in range(len(table[i])):
                w = table[i][j]
                w_class = w.winfo_class()
                columnspan = 3 - len(table[i])
                if w_class == 'TLabel':
                    if i == 0:
                        w['style'] = 'subfield.' + w_class
                    elif i % 2 == 1:
                        w['style'] = 'grey_alt_1.' + w_class
                    else:
                        w['style'] = 'grey_alt_2.' + w_class
                table[i][j].grid(row=i, column=j, columnspan=columnspan, sticky=W+E+N+S, padx=2, pady=1)

    def to_edit_mode(self):
        frame = self.right
        frame.cleanup()

        label = self.get_label_dict(frame, [name_, due_date_, priority_, picture_, money_, contact_info_]) 
        form_dict, widget_dict = self.get_form_dict(self.right, self.current_item)
        update_button = Button(frame, text='Update!',
                               command=(lambda id=self.current_item.id, form_dict=form_dict:
                                        self.controller.update_item(id, values=self.get_update_item_values(form_dict))))
        remove_button = Button(frame, text='Remove',
                               command=(lambda id=self.current_item.id: self.controller.remove_item(id)))

        table = [[label[name_], widget_dict[name_]],
                 [label[due_date_], widget_dict[due_date_][month_],
                  widget_dict[due_date_][day_], widget_dict[due_date_][year_]],
                 [label[priority_], widget_dict[priority_]],
                 # [label[picture_], widget_dict[picture_]],
                 [label[money_], widget_dict[money_]],
                 [label[contact_info_], widget_dict[contact_info_]],
                 [update_button],
                 [remove_button]]

        for i in range(len(table)):
            for j in range(len(table[i])):
                w = table[i][j]
                w_class = w.winfo_class()
                if (j == 0) and (w_class == 'TLabel'):
                    if i % 2 == 1:
                        w['style'] = 'grey_alt_1.' + w_class
                    else:
                        w['style'] = 'grey_alt_2.' + w_class
                if i > len(table) - 3:  # If last 2 rows
                    columnspan = 4
                elif j == 0:  # If label column
                    columnspan = 1
                elif len(table[i]) == 2:  # Entry is not due date
                    columnspan = 3
                else:
                    columnspan = 1
                w.grid(row=i, column=j, columnspan=columnspan, sticky=W+E, padx=2, pady=1)

    def get_form_dict(self, frame, item):
        item_dict = self.get_item_dict(item)

        form_dict = {}
        widget_dict = {}

        # Name
        entry = Entry(frame)
        entry.insert(0, item_dict[name_])

        form_dict[name_] = entry
        widget_dict[name_] =entry

        # Due Date
        entry_1 = Entry(frame, width=3)
        entry_2 = Entry(frame, width=3)
        entry_3 = Entry(frame, width=3)

        due_date = item_dict[due_date_]
        if due_date is None:
            entry_1.insert(0, 'Month')
            entry_2.insert(0, 'Day')
            entry_3.insert(0, 'Year')
        else:
            entry_1.insert(0, due_date.month)
            entry_2.insert(0, due_date.day)
            entry_3.insert(0, due_date.year)

        form_dict[due_date_] = {month_: entry_1, day_: entry_2, year_: entry_3}
        widget_dict[due_date_] = {month_: entry_1, day_: entry_2, year_: entry_3}

        # Priority
        priorities = [none_str_]
        for priority in self.priority_list:
            priorities.append(priority.name)
        
        variable = StringVar(frame)
        if item_dict[priority_] is None:
            variable.set(none_str_)
        else:
            variable.set(item_dict[priority_].name)

        option_menu = OptionMenu(frame, variable, *priorities)

        form_dict[priority_] = variable
        widget_dict[priority_] = option_menu

        # Image
        #form_dict[picture_] = None
        #widget_dict[picture_] = None 

        # Money
        entry = Entry(frame)
        if item_dict[money_] is not None:
            entry.insert(0, item_dict[money_].amount)

        form_dict[money_] = entry
        widget_dict[money_] = entry

        # Contact Info
        contact_infos = [none_str_]
        for contact_info in self.contact_info_book:
            contact_infos.append(contact_info.name)

        variable = StringVar(frame)
        if item_dict[contact_info_] is None:
            variable.set(none_str_)
        else:
            variable.set(item_dict[contact_info_].name)

        option_menu = OptionMenu(frame, variable, *contact_infos)

        form_dict[contact_info_] = variable
        widget_dict[contact_info_] = option_menu

        return form_dict, widget_dict

    def get_update_item_values(self, form_dict):
        values = {}

        # Name
        values[name_] = form_dict[name_].get()

        # Due Date
        values[due_date_] = {}
        for part in [month_, day_, year_]:
            input = form_dict[due_date_][part].get()
            if input == '':
                values[due_date_] = None
                break
            try:
                values[due_date_][part] = int(input)
            except ValueError:
                values[due_date_] = None
                break

        # Priority
        values[priority_] = form_dict[priority_].get()

        # Image
        #

        # Money
        input = form_dict[money_].get()
        if input == '':
            values[money_] = None
        else:
            values[money_] = float(input)

        # Contact Info
        values[contact_info_] = form_dict[contact_info_].get()

        return values
