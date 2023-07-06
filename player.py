class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = None

    def move(self, location):
        self.location = location

    def take_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        # Implement item usage logic
        pass
