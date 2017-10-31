from datetime import date

from item_type import *
from item import *
from priority import *
from money import *
from phone import *
from address import *
from contact_info import *

item_type_check = ItemType(0, 'check')
item_type_note = ItemType(1, 'note')

date1 = date(2017, 10, 30)
date2 = date(2017, 12, 20)

priority_high = Priority(0, 'high', 1)
priority_normal = Priority(1, 'normal', 2)
priority_low = Priority(2, 'low', 3)

money1 = Money(935)

phone1 = Phone('1234567890')
address1 = Address('3 Fun St', 'Yum City', 'CA', '98765')
contact_info1 = ContactInfo('cafe', phone1, address1)

item1 = Item(3, 'hohoho', item_type_check, None, 
            date1, date2, priority_high, None, 
            money1, contact_info1)

item2 = Item(777, 'ponyo', item_type_note, item1, 
            date1, date2, priority_low, None, 
            None, None)

#print(item1)
#print(item2)

from list import *

list = List()
list.add_item('Example1', item_type_check, None, date(2017, 11, 11),
              priority_low, None, money1, contact_info1)
list.add_item('Example2', item_type_note, item1, date(2017, 12, 20),
              priority_normal, None, None, None)
print(list)
