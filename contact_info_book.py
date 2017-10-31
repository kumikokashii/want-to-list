from contact_info import *

class ContactInfoBook():
    def __init__(self):
        self.book = []

    def __str__(self):
        output = ''
        for contact_info in self.book:
            output += str(contact_info)
            output += '\n'
        return output

    def add(self, contact_info):
        self.book.append(contact_info)

    def set_default(self):
        self.book = []
        self.add(ContactInfo(name='Habbit Burger', phone='1234567890', address=None))
