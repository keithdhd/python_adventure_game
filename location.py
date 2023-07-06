class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_locations = {}
        self.items = []

    def add_connection(self, direction, location):
        self.connected_locations[direction] = location

    def get_description(self):
        desc = self.description

        if len(self.items) > 0:
            desc += " You can see "
            for item in self.items:
                desc += item.description

        return desc

    def add_item(self, item):
        self.items.append(item)
