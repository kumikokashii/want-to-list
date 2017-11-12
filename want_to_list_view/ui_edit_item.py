from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image

from str_vars import *
from .ui_tab_in_notebook import *

class UIEditItem(UIFrame):
    def __init__(self, ui_item_list):
        super().__init__(ui_item_list)
        self.controller = ui_item_list.controller
        self.priority_list = ui_item_list.priority_list
        self.contact_info_book = ui_item_list.contact_info_book
        self.item = None 

    def refresh(self, item):
        self.item = item
        self.cleanup() 

        pieces = self.get_pieces()
        form_dict = self.get_form_dict(pieces)
        self.add_buttons_to_pieces(pieces, form_dict)

        parts = self.get_parts(pieces)
        self.make_grid(parts)

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

    def get_pieces(self):
        item = self.item

        label = self.get_label_dict(self, [name_, due_date_, priority_, picture_,
                                           money_, contact_info_]) 
        pieces = {}

        # Name
        entry = Entry(self)
        entry.insert(0, item.name) 
        pieces[name_] = [label[name_], entry]

        # Due date
        entry_1 = Entry(self, width=3)
        entry_2 = Entry(self, width=3)
        entry_3 = Entry(self, width=3)

        due_date = item.due_date
        if due_date is None:
            entry_1.insert(0, 'Month')
            entry_2.insert(0, 'Day')
            entry_3.insert(0, 'Year')
        else:
            entry_1.insert(0, due_date.month)
            entry_2.insert(0, due_date.day)
            entry_3.insert(0, due_date.year)

        pieces[due_date_] = [label[due_date_], entry_1, entry_2, entry_3]

        # Priority
        priorities = [none_str_]
        for priority in self.priority_list:
            priorities.append(priority.name)
        
        variable = StringVar(self)
        if priority is None:
            variable.set(none_str_)
        else:
            variable.set(priority.name)

        option_menu = OptionMenu(self, variable, *priorities)

        pieces[priority_] = [label[priority_], option_menu, variable]

        # Picture
        label_pic = ttk.Label(self)  # Label to contain a picture
        label_path = ttk.Label(self, text='')  # Hidden label to store path to uploaded pic

        if item.picture is not None:
            tk_image = self.get_resized_tk_image(item.picture, 50)
            label_pic.configure(image=tk_image)
            label_pic.image = tk_image

        up_button = Button(self, text='↑',
                           command=lambda label=label, label_path=label_path:
                                   self.upload_img_onclick(label_pic, label_path))

        x_button = Button(self, text=remove_str_,
                          command=lambda label=label, label_path=label_path:
                                  self.remove_img_onclick(label_pic, label_path))

        pieces[picture_] = [label[picture_], label_pic, up_button, x_button, label_path]

        # Money
        entry = Entry(self)
        if item.money is not None:
            entry.insert(0, item.money.amount)        

        pieces[money_] = [label[money_], entry]

        # Contact info
        contact_infos = [none_str_]
        for contact_info in self.contact_info_book:
            contact_infos.append(contact_info.name)

        variable = StringVar(self)
        if item.contact_info is None:
            variable.set(none_str_)
        else:
            variable.set(item.contact_info.name)

        option_menu = OptionMenu(self, variable, *contact_infos)

        pieces[contact_info_] = [label[contact_info_], option_menu, variable]

        return pieces

    def get_form_dict(self, pieces):
        form_dict = {}

        for field in pieces:
            if field in [priority_, picture_, contact_info_]:
                content = pieces[field][-1]
            else:
                content = pieces[field][1:]

            # If only one element in list, take away list
            if isinstance(content, list) and (len(content) == 1):
                content = content[0]

            # Break up dates into dict
            if field == due_date_:
                month, day, year = content
                content = {month_: month, day_: day, year_: year}

            form_dict[field] = content

        return form_dict       

    def add_buttons_to_pieces(self, pieces, form_dict):
        id = self.item.id

        # Update button
        update_button = Button(self, text='Update!',
                               command=(lambda id=id, form_dict=form_dict:
                                        self.controller.update_item(id, values=self.get_update_item_values(form_dict))))
        pieces['update'] = update_button

        # Remove button
        remove_button = Button(self, text='Remove',
                               command=(lambda id=id: self.controller.remove_item(id)))
        pieces['remove'] =remove_button

    def get_parts(self, pieces):
        parts = {}

        for field in pieces:
            if field in [priority_, picture_, contact_info_]:
                parts[field] = pieces[field][:-1]
            else:
                parts[field] = pieces[field]

        return parts

    def make_grid(self, parts):
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
