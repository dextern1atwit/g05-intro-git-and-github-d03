from room import Room


class Player:

  def __init__(self, starting_room):
    self.location = starting_room
    self.inventory = []
    self.inventory_disp = []
    self.health = 3
    self.hasKey = False
    self.hasSword = False
    self.hasShield = False

  def display_status(self):
    print(f"Description: {self.current_room.description}")
    print(f"Health: {self.health}")
    print(f"Inventory: {self.inventory_disp}")

  def move(self, direction):
    if direction.lower() == 'north' and self.current_room.north:
      self.current_room = self.current_room.north
      print("You move to the north.")
      print(self.current_room.description)
      self.current_room.roomCheck(self.current_room, self)
    elif direction.lower() == 'south' and self.current_room.south:
      self.current_room = self.current_room.south
      print("You move to the south.")
      self.current_room.roomCheck(self.current_room, self)
    elif direction.lower() == 'east' and self.current_room.east:
      self.current_room = self.current_room.east
      print("You move to the east.")
      self.current_room.roomCheck(self.current_room, self)
    elif direction.lower() == 'west' and self.current_room.west:
      self.current_room = self.current_room.west
      print("You move to the west.")
      self.current_room.roomCheck(self.current_room, self)
    else:
      print(f"There is no path to the {direction}.")
