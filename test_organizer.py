from organizer import *

organizer = Organizer()
organizer.load_default()

item1 = organizer.list.list[0]
item1.toggle_check()

print(organizer.item_type_list)
print(organizer.priority_list)
print(organizer.contact_info_book)
print(organizer.list)


