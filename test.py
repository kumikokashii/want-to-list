from phone import *

phone = Phone('1234567890')
#print(phone)

################################
from address import *

address = Address('935 Fun', 'Yay City', 'CA', '12345')
#print(address.concat())

address = Address('', 'Yay City', '', '12345')
#print(address.concat())

################################
from contact_info import *

contact_info = ContactInfo('Cup', phone, address)
#print(contact_info.name)
#print(contact_info.phone)
#print(contact_info.address.concat())

################################
from money import *

spend = Money(4.355)
#print(spend.concat())

################################
from priority import *

priority = Priority(0, 'normal', 2)
#print(priority)
priority.set_name('super important')
#print(priority)

################################
from item_type import *

item_type = ItemType()
#print(item_type.name)
item_type.set_name('note')
#print(item_type.name)

################################
from item import *

item = Item('First Item!', '', '', '', '', '', '', '')
#print(item.name)
#print(item.created_date)

from list import *

list = List()
#print(list.list)
list.add_item(item)
#print(list.list[0].name)

################################
from priority_list import *

priority_list = PriorityList()
#print(priority_list)

priority_high = Priority(0, 'high', 1)
priority_list.add(priority_high)

priority_normal = Priority(1, 'normal', 2)
priority_list.add(priority_normal)

priority_okay = Priority(2, 'okay', 3)
priority_list.add(priority_okay)

print(priority_list)
print()

new_list = ((0, 'super', 1), (1, 'normal', 2), (2, 'okay', 3))
priority_list.edit(new_list)
print(priority_list)
print()

new_list = ((0, 'super', 1), (1, 'normal', 2), (2, 'okay', 3), (3, 'hmm', 4))
priority_list.edit(new_list)
print(priority_list)
print()

new_list = ((0, 'super', 1), (1, 'normal', 2), (2, 'ha!', 4))
priority_list.edit(new_list)
print(priority_list)
print()
