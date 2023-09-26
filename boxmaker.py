import rhinoscriptsyntax as rs

#I don't want to type out this massive line ever again so I'm making a function
def makeBox(x, y, z, l, w, h):
    rs.AddBox([[x, y+w, z], [x, y, z], [x+l, y, z], [x+l, y+w, z], [x, y+w, z+h], [x, y, z+h], [x+l, y, z+h], [x+l, y+w, z+h]])

if __name__ == "__main__":
    makeBox(0, 0, 0, 10, 10, 10)