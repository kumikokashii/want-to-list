
class Phone():
    def __init__(self, digits):
        # Assumes digits is a string of 10 digits
        self.area_code = digits[0: 3]  # First 3 digits
        self.prefix = digits[3: 6]  # Next 3 digits
        self.line = digits[6: 10]  # Last 4 digits

    def __str__(self):
        return '(' + self.area_code + ')' + self.prefix + '-' + self.line
