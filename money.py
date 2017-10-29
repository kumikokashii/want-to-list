
class Money():
    def __init__(self, amount, unit='$'):
        self.amount = amount  # Numeric
        self.unit = unit

    def concat(self):
        if self.unit == '$':
            return self.unit + '{:.2f}'.format(self.amount)
