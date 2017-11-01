
class IncrementalIDList(list):
    def __init__(self):
        super().__init__()

    def __str__(self):
        output = ''
        for elem in self:
            output += str(elem)
            output += '\n'
        return output

    def get_next_id(self):
        max_id = -1
        for elem in self:
            if elem.id > max_id:
                max_id = elem.id
        return max_id + 1

    def get_elem_by_id(self, id):
        for elem in self:
            if elem.id == id:
                return elem
        return None

    def get_elem_by_name(self, name):
        for elem in self:
            if elem.name == name:
                return elem
        return None
