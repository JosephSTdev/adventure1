class Room:
    def __init__(self, descriptiveText, adjacentRooms=[]):
        self.text = descriptiveText
        self.nextRooms = []
        for x in adjacentRooms:
            self.nextRooms.append(x)
  #  def addPath(self, roomB):
  #      self.nextRooms.append()