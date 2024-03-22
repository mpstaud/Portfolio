
class Produce:
    def __init__(self, name, category):
        self.name = name
        self.category = category


class Protein:
    def __init__(self, name, category):
        self.name = name
        self.category = category


Apple = Produce('Apple', 'Fruit')
Banana = Produce('Banana', 'Fruit')
Grapes = Produce('Grapes', 'Fruit')
Carrots = Produce('Carrots', 'Vegetable')
g = [vars(Apple), vars(Banana), vars(Carrots)]
print(g[0])
