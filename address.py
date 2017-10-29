
class Address():
    def __init__(self, street_address, city, state, zip_code):
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def concat(self):
        address = self.street_address
        if self.city != '':
            if self.street_address != '':
                address += ', '
            address += self.city
        if self.state != '':
            if (self.street_address != '') or (self.city != ''):    
                address += ', '
            address += self.state
        if self.zip_code != '':
            if self.state != '':
                address += ' '
            elif (self.street_address != '') or (self.city != ''):
                address += ', '
            address += self.zip_code
        return address
