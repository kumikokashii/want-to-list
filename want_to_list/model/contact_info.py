
class ContactInfo():
    def __init__(self, id, name, phone, address):
        self.id = id  # int
        self.name = name  # str
        self.phone = phone  # Phone
        self.address = address  # Address

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + str(self.phone) + ' ' + str(self.address)

    def block_str(self):
        output = self.name + '\n'
        output += str(self.phone) + '\n'
        output += self.address.block_str()
        return output
