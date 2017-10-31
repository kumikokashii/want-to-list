
class Money():
    def __init__(self, amount, unit='$'):
        self.amount = amount  # numeric
        self.unit = unit  # str

    def __str__(self):
        if self.unit == '$':
            return self.unit + '{:.2f}'.format(self.amount)
