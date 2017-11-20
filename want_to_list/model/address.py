
class Address():
    def __init__(self, street_address, city, state, zip_code):
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        output = self.street_address
        if self.city != '':
            if self.street_address != '':
                output += ', '
            output += self.city
        if self.state != '':
            if (self.street_address != '') or (self.city != ''):    
                output += ', '
            output += self.state
        if self.zip_code != '':
            if self.state != '':
                output += ' '
            elif (self.street_address != '') or (self.city != ''):
                output += ', '
            output += self.zip_code
        return output

    def block_str(self):
        output = ''
        if self.street_address != '':
            output += self.street_address + '\n'
        if (self.city != '') or (self.state != ''):
            if self.city != '':
                output += self.city
                if self.state != '':
                    output += ', ' + self.state
            else:
                output += self.state
            output += '\n'
        if self.zip_code != '':
            output += self.zip_code
        return output

