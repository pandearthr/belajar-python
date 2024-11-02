class parent(object):
    def __init__(self):
        self.value = 4
    def get_value(self):
        return self.value

parent1 = parent()
print("parent : ", parent1.get_value())

class child(parent):
    def get_value(self):
        return self.value + 1

child1 = child()
print("child : ", child1.get_value())