
from tkinter import *
from tkinter import ttk

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

        self._none_str = '-' 
        self._name = 'Name'
        self._due_date = 'Due'
        self._priority = 'Priority'
        self._picture = 'Img'
        self._money = 'Money'
        self._contact_info = 'Contact Info'
        self._created_date = 'Created on'

        self._month = 'Month'
        self._day = 'Day'
        self._year = 'Year'

    def get_item_dict(self, item):
        item_dict = {self._name: item.name,
                     self._due_date: item.due_date,
                     self._priority: item.priority,
                     self._picture: item.picture,
                     self._money: item.money,
                     self._contact_info: item.contact_info,
                     self._created_date: item.created_date}
        return item_dict
        
    def refresh_left(self):
        frame = self.left
        frame.cleanup() 

        table = []

        # List name
        if self.current_list.id != 0:  # If not top level
            parent_id = self.current_list.parent.id
            label_1 = Label(frame, text='^')
            label_1.bind('<Button-1>', lambda event, id=parent_id: self.controller.onclick_item(id))

            label_2 = Label(frame, text=self.current_list.name)
            label_2.bind('<Button-1>', lambda event, id=self.current_list.id: self.controller.onclick_title(id))
            table.append([label_1, label_2])

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

            label = Label(frame, text=name)
            label.bind('<Button-1>', lambda event, id=id: self.controller.onclick_item(id))

            table.append([check_button, label])

        # Add new item
        add_button = Button(frame, text='+')
        entry = Entry(frame)
        add_button.bind('<Button-1>', lambda event, entry=entry: self.controller.add_item(entry.get()))
        table.append([add_button, entry])

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

    def refresh_right(self):
        frame = self.right
        frame.cleanup()

        if self.current_item.id == 0:  # If top level
            return

        item = self.current_item
        item_dict = self.get_item_dict(item)
        format_dict = {self._due_date: (lambda due_date: '{:%a, %b %-d, %Y}'.format(due_date)),
                       self._priority: (lambda priority: priority.name),
                       self._money: (lambda money: str(money)),
                       self._contact_info: (lambda contact_info: contact_info.block_str()),
                       self._created_date: (lambda created_date: '{:%-m/%-d/%Y %-I:%M%p}'.format(created_date))}

        table = []

        # Name & Edit button
        label = Label(frame, text=item_dict[self._name])
        edit_button = Button(frame, text='Edit me')
        edit_button.bind('<Button-1>', lambda event: self.to_edit_mode())
        table.append([label, edit_button])

        # Details
        for field in [self._due_date, self._priority, self._picture, self._money, self._contact_info, self._created_date]:
            content = item_dict[field]
            if content is None:
                continue

            format = format_dict[field]
            value = format(content)
            label_1 = Label(frame, text=field)
            label_2 = Label(frame, text=value)
            table.append([label_1, label_2])

        # Add new item
        if len(self.current_item) == 0:  # If has no item
            add_button = Button(frame, text='+')
            entry = Entry(frame)
            add_button.bind('<Button-1>', lambda event, entry=entry: self.controller.add_child(entry.get()))
            table.append([add_button, entry])

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

    def to_edit_mode(self):
        frame = self.right
        frame.cleanup()

        label = self.get_label_dict(self.right) 
        form_dict, widget_dict = self.get_form_dict(self.right, self.current_item)
        update_button = Button(frame, text='Update!', command=(lambda id=self.current_item.id, form_dict=form_dict: self.controller.update_item(id, values=self.get_update_item_values(form_dict))))

        table = [[label[self._name], widget_dict[self._name]],
                 [label[self._due_date], widget_dict[self._due_date][self._month],
                  widget_dict[self._due_date][self._day], widget_dict[self._due_date][self._year]],
                 [label[self._priority], widget_dict[self._priority]],
                 # [label[self._picture], widget_dict[self._picture]],
                 [label[self._money], widget_dict[self._money]],
                 [label[self._contact_info], widget_dict[self._contact_info]],
                 [update_button]]

        for i in range(len(table)):
            for j in range(len(table[i])):
                table[i][j].grid(row=i, column=j)

    def get_label_dict(self, frame):
        label = {}
        for field in [self._name, self._due_date, self._priority, self._picture, self._money, self._contact_info]:
            label[field] = Label(frame, text=field)
        return label

    def get_form_dict(self, frame, item):
        item_dict = self.get_item_dict(item)

        form_dict = {}
        widget_dict = {}

        # Name
        entry = Entry(frame)
        entry.insert(0, item_dict[self._name])

        form_dict[self._name] = entry
        widget_dict[self._name] =entry

        # Due Date
        entry_1 = Entry(frame)
        entry_2 = Entry(frame)
        entry_3 = Entry(frame)

        due_date = item_dict[self._due_date]
        if due_date is None:
            for entry in [entry_1, entry_2, entry_3]:
                entry.insert(0, '')
        else:
            entry_1.insert(0, due_date.month)
            entry_2.insert(0, due_date.day)
            entry_3.insert(0, due_date.year)

        form_dict[self._due_date] = {self._month: entry_1, self._day: entry_2, self._year: entry_3}
        widget_dict[self._due_date] = {self._month: entry_1, self._day: entry_2, self._year: entry_3}

        # Priority
        priorities = [self._none_str]
        for priority in self.priority_list:
            priorities.append(priority.name)
        
        variable = StringVar(frame)
        if item_dict[self._priority] is None:
            variable.set(self._none_str)
        else:
            variable.set(item_dict[self._priority].name)

        option_menu = OptionMenu(frame, variable, *priorities)

        form_dict[self._priority] = variable
        widget_dict[self._priority] = option_menu

        # Image
        #form_dict[self._picture] = None
        #widget_dict[self._picture] = None 

        # Money
        entry = Entry(frame)
        if item_dict[self._money] is not None:
            entry.insert(0, item_dict[self._money].amount)

        form_dict[self._money] = entry
        widget_dict[self._money] = entry

        # Contact Info
        contact_infos = [self._none_str]
        for contact_info in self.contact_info_book:
            contact_infos.append(contact_info.name)

        variable = StringVar(frame)
        if item_dict[self._contact_info] is None:
            variable.set(self._none_str)
        else:
            variable.set(item_dict[self._contact_info].name)

        option_menu = OptionMenu(frame, variable, *contact_infos)

        form_dict[self._contact_info] = variable
        widget_dict[self._contact_info] = option_menu

        return form_dict, widget_dict

    def get_update_item_values(self, form_dict):
        values = {}

        # Name
        values[self._name] = form_dict[self._name].get()

        # Due Date
        values[self._due_date] = {}
        for part in [self._month, self._day, self._year]:
            input = form_dict[self._due_date][part].get()
            if input == '':
                values[self._due_date] = None
                break
            values[self._due_date][part] = int(input)

        # Priority
        values[self._priority] = form_dict[self._priority].get()

        # Image
        #

        # Money
        input = form_dict[self._money].get()
        if input == '':
            values[self._money] = None
        else:
            values[self._money] = int(input)

        # Contact Info
        values[self._contact_info] = form_dict[self._contact_info].get()

        return values
