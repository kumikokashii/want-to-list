
from tkinter import *
from tkinter import ttk

from str_vars import *
from .ui_tab_in_notebook import *

class UIItemList(UITabInNB):
    def __init__(self, parent, tab_name, organizer): 
        super().__init__(parent, tab_name)
        self.item_list = organizer.item_list
        self.priority_list = organizer.priority_list
        self.contact_info_book = organizer.contact_info_book
        self.left = UIFrame(self)
        self.left.grid(row=0, column=0)
        self.right = UIFrame(self)
        self.right.grid(row=0, column=1)
        self.current_list = self.item_list.root
        self.current_item = self.item_list.root
        self.sort_key = 'name'

    def get_item_dict(self, item):
        item_dict = {name_: item.name,
                     due_date_: item.due_date,
                     priority_: item.priority,
                     picture_: item.picture,
                     money_: item.money,
                     contact_info_: item.contact_info,
                     created_date_: item.created_date}
        return item_dict
        
    def refresh_left(self):
        frame = self.left
        frame.cleanup() 

        table = []

        # List name
        if self.current_list.id != 0:  # If not top level
            parent_id = self.current_list.parent.id
            up_button = Button(frame, text='^')
            up_button.bind('<Button-1>', lambda event, id=parent_id: self.controller.onclick_item(id))

            label = ttk.Label(frame, text=self.current_list.name)
            label.bind('<Button-1>', lambda event, id=self.current_list.id: self.controller.onclick_title(id))
            table.append([up_button, label])

        # Items
        sorted = self.current_list.get_sorted_by(self.sort_key)
        for item in sorted:
            id = item.id
            is_checked = item.is_checked
            name = item.name

            check_button = Checkbutton(frame)
            if is_checked:
                check_button.select()
            check_button.bind('<Button-1>', lambda event, id=id: self.controller.toggle_check(id))

            label = ttk.Label(frame, text=name)
            label.bind('<Button-1>', lambda event, id=id: self.controller.onclick_item(id))

            table.append([check_button, label])

        # Add new item
        add_button = Button(frame, text='+')
        entry = Entry(frame)
        add_button.bind('<Button-1>', lambda event, entry=entry: self.controller.add_item(entry.get(), self.current_list))
        table.append([add_button, entry])

        for i in range(len(table)):
            for j in range(len(table[i])):
                w = table[i][j]
                w_class = w.winfo_class()
                if (j == 1) & (w_class == 'TLabel'):
                    if (self.current_list.id != 0) & (i == 0): 
                        w['style'] = 'field.' + w_class
                    elif i % 2 == 1:
                        w['style'] = 'alt_1.' + w_class
                    else:
                        w['style'] = 'alt_2.' + w_class
                w.grid(row=i, column=j, sticky=W+E, padx=2, pady=1)

    def refresh_right(self):
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

        # Name & Edit button
        label = ttk.Label(frame, text=item_dict[name_])
        edit_button = Button(frame, text='Edit me')
        edit_button.bind('<Button-1>', lambda event: self.to_edit_mode())
        table.append([label, edit_button])

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
                if w_class == 'TLabel':
                    if i == 0:
                        w['style'] = 'subfield.' + w_class
                    elif i % 2 == 1:
                        w['style'] = 'alt_1.' + w_class
                    else:
                        w['style'] = 'alt_2.' + w_class
                table[i][j].grid(row=i, column=j, sticky=W+E+N+S, padx=2, pady=1)

    def to_edit_mode(self):
        frame = self.right
        frame.cleanup()

        label = self.get_label_dict(frame, [name_, due_date_, priority_, picture_, money_, contact_info_]) 
        form_dict, widget_dict = self.get_form_dict(self.right, self.current_item)
        update_button = Button(frame, text='Update!',
                               command=(lambda id=self.current_item.id, form_dict=form_dict:
                                        self.controller.update_item(id, values=self.get_update_item_values(form_dict))))

        table = [[label[name_], widget_dict[name_]],
                 [label[due_date_], widget_dict[due_date_][month_],
                  widget_dict[due_date_][day_], widget_dict[due_date_][year_]],
                 [label[priority_], widget_dict[priority_]],
                 # [label[picture_], widget_dict[picture_]],
                 [label[money_], widget_dict[money_]],
                 [label[contact_info_], widget_dict[contact_info_]],
                 [update_button]]

        for i in range(len(table)):
            for j in range(len(table[i])):
                w = table[i][j]
                w_class = w.winfo_class()
                if (j == 0) and (w_class == 'TLabel'):
                    if i % 2 == 1:
                        w['style'] = 'alt_1.' + w_class
                    else:
                        w['style'] = 'alt_2.' + w_class
                w.grid(row=i, column=j, sticky=W+E, padx=2, pady=1)

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
        entry_1 = Entry(frame)
        entry_2 = Entry(frame)
        entry_3 = Entry(frame)

        due_date = item_dict[due_date_]
        if due_date is None:
            for entry in [entry_1, entry_2, entry_3]:
                entry.insert(0, '')
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
            values[due_date_][part] = int(input)

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
