
class Priority():
    def __init__(self, id, name, importance):
        self.id = id 
        self.name = name
        self.importance = importance

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + str(self.importance)

