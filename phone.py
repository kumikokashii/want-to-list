
class Phone():
    def __init__(self, input):
        # Assumes input is 10 digits
        self.area_code = input[0: 3]  # First 3 digits
        self.prefix = input[3: 6]  # Next 3 digits
        self.line = input[6: 10]  # Last 4 digits
        self.number = '(' + self.area_code + ')' + self.prefix + '-' + self.line

    def __str__(self):
        return self.number
