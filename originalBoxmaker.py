import rhinoscriptsyntax as rs

class box():

    def __init__(self, pos, size):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.l = size[0]
        self.w = size[1]
        self.h = size[2]

    def makeBox(self):
        rs.AddBox([[self.x, self.y+self.w, self.z], [self.x, self.y, self.z], [self.x+self.l, self.y, self.z], [self.x+self.l, self.y+self.w, self.z], [self.x, self.y+self.w, self.z+self.h], [self.x, self.y, self.z+self.h], [self.x+self.l, self.y, self.z+self.h], [self.x+self.l, self.y+self.w, self.z+self.h]])

newBox = box([0, 0, 0], [10, 10, 10])
newBox.makeBox()