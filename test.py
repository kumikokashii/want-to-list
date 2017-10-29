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

priority = Priority('not important')
#print(priority.name)
priority.set_name('super important')
#print(priority.name)

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
print(list.list)
list.add_item(item)
print(list.list[0].name)


