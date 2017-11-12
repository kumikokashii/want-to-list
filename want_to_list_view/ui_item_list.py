
from tkinter import *
from tkinter import ttk, filedialog

from PIL import Image, ImageTk
import datetime

from str_vars import *
from .ui_tab_in_notebook import *

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

    def get_item_name(self, item):
        name = item.name 
        if self.show == 'current list only':
            return name
        parent = item.parent
        if parent.id == 0:  # If top level
            return name
        return name + ' [' + parent.name + ']'

    def refresh_left(self, new_list=None):
        if new_list is not None:
            self.current_list = new_list
        frame = self.left
        frame.cleanup() 

        # Get items to display
        if self.show == 'current list only':
            sorted = self.current_list.get_sorted_with_label_text_by(self.sort_key)
        if self.show == 'all under this list':
            sorted = self.current_list.get_all_childless_items().get_sorted_with_label_text_by(self.sort_key)

        parts = self.get_left_parts(frame, self.current_list, sorted)
        self.make_grid_refresh_left(parts)

    def get_left_parts(self, frame, item, sorted):
        parts = {}

        # Show
        label = ttk.Label(frame, text='show')

        variable = StringVar(frame)
        variable.set(self.show)
        variable.trace('w', lambda _0, _1, _2, show_var=variable: self.show_onchange(show_var))

        options = ['current list only', 'all under this list']
        option_menu = OptionMenu(frame, variable, *options)
        parts['show'] = [label, option_menu]

        # Sort by
        label = ttk.Label(frame, text='sort by')

        variable = StringVar(frame)
        variable.set(self.sort_key)
        variable.trace('w', lambda _0, _1, _2, sort_by_var=variable: self.sort_by_onchange(sort_by_var))

        options = [name_, due_date_, priority_, created_date_]
        option_menu = OptionMenu(frame, variable, *options)
        parts['sort'] = [label, option_menu]

        # Up button and List name
        if item.id != 0:  # If not top level
            parent_id = item.parent.id
            up_button = Button(frame, text='^')
            up_button.bind('<Button-1>', lambda event, id=parent_id: self.controller.onclick_item(id))

            label = ttk.Label(frame, text=item.name)
            label.bind('<Button-1>', lambda event, id=item.id: self.controller.onclick_title(id))
            parts['list name'] = [up_button, label]

        # List block
        list_block = []

        for group, items in sorted:
            if group is not None:  # Create label
                if isinstance(group, datetime.date):  # Format date
                    group = '{:%a, %b %-d, %Y}'.format(group)
                label = ttk.Label(frame, text=group)
            group_label = None if (group is None) else label

            group_items = []
            for item in items:
                # Check button
                check_button = Checkbutton(frame)
                if item.is_checked:
                    check_button_select()
                check_button.bind('<Button-1>', lambda event, id=item.id: self.controller.toggle_check(id))

                # Item name
                name = self.get_item_name(item)
                item_label = ttk.Label(frame, text=name)
                item_label.bind('<Button-1>', lambda event, id=item.id: self.controller.onclick_item(id))

                group_items.append((check_button, item_label))

            list_block.append((group_label, group_items))

        parts['list block'] = list_block

        # Add new item
        add_button = Button(frame, text='+')
        entry = Entry(frame)
        add_button.bind('<Button-1>', lambda event, entry=entry: self.controller.add_item(entry.get(), item))
        parts['add'] = [add_button, entry]

        return parts

    def make_grid_refresh_left(self, parts):
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

    def get_resized_tk_image(self, pil_image, side_max):
        image = pil_image.copy()
        image.thumbnail((side_max, side_max), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    def refresh_right(self, new_item=None):
        if new_item is not None:
            self.current_item = new_item
        frame = self.right
        frame.cleanup()

        if self.current_item.id == 0:  # If top level
            return

        parts = self.get_show_details_parts(frame, self.current_item)
        self.make_grid_refresh_right(parts)

    def make_grid_refresh_right(self, parts):
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

    def get_show_details_parts(self, frame, item):
        item_dict = self.get_item_dict(item)
        format_dict = {due_date_: (lambda due_date: '{:%a, %b %-d, %Y}'.format(due_date)),
                       priority_: (lambda priority: priority.name),
		       picture_: (lambda picture: self.get_resized_tk_image(picture, 200)),
                       money_: (lambda money: str(money)),
                       contact_info_: (lambda contact_info: contact_info.block_str()),
                       created_date_: (lambda created_date: '{:%-m/%-d/%Y %-I:%M%p}'.format(created_date))}

        parts = {}

        # Name
        name = self.get_item_name(item)
        parts[name_] = ttk.Label(frame, text=name)

        # Details
        for field in [due_date_, priority_, picture_, money_, contact_info_, created_date_]:
            content = item_dict[field]
            if content is None:
                continue

            format = format_dict[field]
            value = format(content)
            label_1 = ttk.Label(frame, text=field)
            if field == picture_:
                label_2 = ttk.Label(frame, image=value)
                label_2.image = value
            else:
                label_2 = ttk.Label(frame, text=value)
            parts[field] = [label_1, label_2]

        # Edit button
        edit_button = Button(frame, text='Edit me')
        edit_button.bind('<Button-1>', lambda event: self.to_edit_mode())
        parts['edit'] = edit_button

        # Add new item
        if len(item) == 0:  # If has no item
            add_button = Button(frame, text='+')
            entry = Entry(frame)
            add_button.bind('<Button-1>', lambda event, entry=entry: self.controller.add_child(entry.get(), item))
            parts['add'] = [add_button, entry]

        return parts

        for i in range(len(table)):
            for j in range(len(table[i])):
                w = table[i][j]
                w_class = w.winfo_class()
                columnspan = 3 - len(table[i])
                if w_class == 'TLabel':
                    if i == 0:
                        w['style'] = 'subfield.' + w_class
                    #elif i % 2 == 1:
                        w['style'] = 'grey_alt_1.' + w_class
                    #else:
                        w['style'] = 'grey_alt_2.' + w_class
                table[i][j].grid(row=i, column=j, columnspan=columnspan, sticky=W+E+N+S, padx=2, pady=1)

    def to_edit_mode(self):
        frame = self.right
        frame.cleanup()

        label = self.get_label_dict(frame, [name_, due_date_, priority_, picture_, money_, contact_info_]) 
        form_dict, widget_dict = self.get_update_form_dict(self.right, self.current_item)
        update_button = Button(frame, text='Update!',
                               command=(lambda id=self.current_item.id, form_dict=form_dict:
                                        self.controller.update_item(id, values=self.get_update_item_values(form_dict))))
        remove_button = Button(frame, text='Remove',
                               command=(lambda id=self.current_item.id: self.controller.remove_item(id)))

        parts = {}
        parts[name_] = (label[name_], widget_dict[name_])
        parts[due_date_] = (label[due_date_], widget_dict[due_date_][month_],
                            widget_dict[due_date_][day_], widget_dict[due_date_][year_])
        parts[priority_] = (label[priority_], widget_dict[priority_])
        parts[picture_] = (label[picture_], widget_dict[picture_]['selected'],
                           widget_dict[picture_]['upload'], widget_dict[picture_]['remove'])
        parts[money_] = (label[money_], widget_dict[money_])
        parts[contact_info_] = (label[contact_info_], widget_dict[contact_info_])
        parts['update'] = update_button
        parts['remove'] = remove_button
        self.make_grid_to_edit_mode(parts)

    def make_grid_to_edit_mode(self, parts):
        row_order = [name_, due_date_, priority_, picture_, money_,
                     contact_info_, 'update', 'remove']

        current_row = 1
        for row_name in row_order:
            # Field name
            if row_name not in ['update', 'remove']:
                label = parts[row_name][0]

                # Row span
                rowspan = 1
                if row_name == picture_:
                    rowspan = 2

                # Color
                ith_field = row_order.index(row_name)
                if ith_field % 2 == 1:
                    label['style'] = 'grey_alt_1.TLabel'
                else:
                    label['style'] = 'grey_alt_2.TLabel'               

                label.grid(row=current_row, column=1, rowspan=rowspan, sticky=W+E+N+S, padx=2, pady=1)

            # User input
            if  row_name in [name_, priority_, money_, contact_info_]:
                label, entered = parts[row_name]
                entered.grid(row=current_row, column=2, columnspan=3, sticky=W+E+N+S, padx=2, pady=1)

            if row_name == due_date_:
                label, e1, e2, e3 = parts[row_name]
                col = 2
                for entered in [e1, e2, e3]:
                    entered.grid(row=current_row, column=col, sticky=W+E+N+S, padx=2, pady=1)
                    col += 1

            if row_name == picture_:
                label, selected, upload, remove = parts[row_name]
                selected.grid(row=current_row, rowspan=2, column=2, columnspan=2, padx=2, pady=1)
                upload.grid(row=current_row, column=4, sticky=W+E, padx=2, pady=1)
                remove.grid(row=current_row+1, column=4, sticky=W+E, padx=2, pady=1)
                current_row += 1  # Extra row

            # Button
            if row_name in ['update', 'remove']:
                button = parts[row_name]
                button.grid(row=current_row, column=1, columnspan=4, sticky=W+E, padx=2, pady=1)
           
            current_row += 1

    def get_update_form_dict(self, frame, item):
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

        # Picture
        label = ttk.Label(frame)  # Label to contain a picture
        label_path = ttk.Label(frame, text='')  # Hidden label to store path to uploaded pic
        if item_dict[picture_] is not None:
            tk_image = self.get_resized_tk_image(item_dict[picture_], 50)
            label.configure(image=tk_image)
            label.image = tk_image

        x_button = Button(frame, text=remove_str_,
                          command=lambda label=label, label_path=label_path:
                                  self.remove_img_onclick(label, label_path))
        up_button = Button(frame, text='↑',
                           command=lambda label=label, label_path=label_path:
                                   self.upload_img_onclick(label, label_path))

        form_dict[picture_] = label_path 
        widget_dict[picture_] = {'selected': label, 'remove': x_button, 'upload': up_button}

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

    def remove_img_onclick(self, label, label_path):
        label.grid_remove()  # With grid_remove, widget remembers its position etc.
                             # With grid_forget, widget forgets all grid options
        label_path.configure(text='remove')

    def upload_img_onclick(self, label, label_path):
        file_path = filedialog.askopenfilename(
                        initialdir = '.',
                        title = 'Select an image!',
                        filetypes = (('jpeg files','*.jpg'), ('all files','*.*')))

        if file_path != '':  # File is selected
            pil_image = Image.open(file_path)
            tk_image = self.get_resized_tk_image(pil_image, 50)
            label.configure(image=tk_image)
            label.image = tk_image
            label.grid()
        label_path.configure(text=file_path)  # '' means same as before

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

        # Picture
        file_path = form_dict[picture_]['text']
        skip_update = False
        picture = None

        if file_path == '':  # Unchanged
            skip_update = True
        elif file_path != 'remove':  # File is specified
            picture = Image.open(file_path)
        values[picture_] = (skip_update, picture)

        # Money
        input = form_dict[money_].get()
        if input == '':
            values[money_] = None
        else:
            values[money_] = float(input)

        # Contact Info
        values[contact_info_] = form_dict[contact_info_].get()

        return values
