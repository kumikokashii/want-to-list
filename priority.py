
class Priority():
    def __init__(self, id, name, importance):
        self.id = id 
        self.name = name
        self.importance = importance

    def __str__(self):
        return self.concat()

    def concat(self):
        return str(self.id) + ' ' + self.name + ' ' + str(self.importance)

    def set_name(self, name):
        self.name = name
