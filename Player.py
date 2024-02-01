import room.Py
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
        self.max_inventory_slots = 5
        self.health = 3

    def display_status(self):
        print(f"{self.name}'s Status:")
        print(f"Current Room: {self.current_room.name}")
        if ((not self.current_room.isDark) and ('torch' not in self.inventory)):
            print(f"Description: {self.current_room.description}")
        print(f"Health: {self.health}")
        print(f"Inventory: {self.inventory}")

    def move(self, direction):
        if direction.lower() == 'north' and self.current_room.north:
            self.current_room = self.current_room.north
            print(f"{self.name} moved to the north.")
            self.current_room.roomCheck(self.current_room, self)
        elif direction.lower() == 'south' and self.current_room.south:
            self.current_room = self.current_room.south
            print(f"{self.name} moved to the south.")
            self.current_room.roomCheck(self.current_room, self)
        elif direction.lower() == 'east' and self.current_room.east:
            self.current_room = self.current_room.east
            print(f"{self.name} moved to the east.")
            self.current_room.roomCheck(self.current_room, self)
        elif direction.lower() == 'west' and self.current_room.west:
            self.current_room = self.current_room.west
            print(f"{self.name} moved to the west.")
            self.current_room.roomCheck(self.current_room, self)
        else:
            print(f"There is no path to the {direction}.")
    
    def hasKey(self):
        if ('key' in self.inventory):
            return True

    def pick_up_item(self, item):
        if len(self.inventory) < self.max_inventory_slots:
            self.inventory.append(item)
            print(f"{self.name} picked up {item}.")
        else:
            print(f"{self.name}'s inventory is full. Cannot pick up {item}.")