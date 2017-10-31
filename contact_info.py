
class ContactInfo():
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone  # Phone
        self.address = address  # Address

    def __str__(self):
        return self.name + ' ' + str(self.phone) + ' ' + str(self.address)

