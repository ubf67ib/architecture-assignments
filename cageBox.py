from boxmaker import *

#It's a function because reasons
def makeCagebox():
    x = y = z = 0
    l = w = h = 10
    lines  = []
    i = 0

    #Layers were a part of the assignment
    outsideBoxes = rs.createColor(124, 150, 255)
    rs.addLayer("BOXES", outsideBoxes)
    rs.currentLayer("BOXES")
    rs.deleteLayer(Default)
    lineColor = rs.createColor(0, 0, 255)
    rs.addLayer("CURVES", lineColor)
    slabColor = rs.createColor(118, 114, 217)
    rs.addLayer("SLABS", slabColor)

    #Create 8 outer boxes
    while z <= 40:
        while x <= 40:
            while y <= 40:
                makeBox(x, y, z, l, w, h)
                y += 40
            x += 40
            y = 0
        z += 40
        x = 0
        y = 0

    #Now create the lines in between the boxes. Why do i need so many lines :((((((
    rs.currentlayer("CURVES")
    x = y = z = 0
    l = w = h = 50
    xOffset = yOffset = zOffset = 50

    for j in range(2):
        while z <= zOffset + z:
            while y <= yOffset + y:
                lines[i] = rs.newLine([[x, y, z], [x+l, y, z]])
                i =+ 1
                y += yOffset
            y = 0
            z += zOffset
        x = y = z = 0

        while z <= zOffset + z:
            while x <= xOffset + x:
                lines[i] = rs.newLine([[x, y, z], [x, y+w, z]])
                i =+ 1
                x += xOffset
            x = 0
            z += zOffset
        x = y = z = 0

        while x <= xOffset + x:
            while y <= yOffset + y:
                lines[i] = rs.newLine([[x, y, z], [x, y, z+h]])
                i =+ 1
                y += yOffset
            y = 0
            x += xOffset
        x = y = z = 0

        if j == 0:
            l = w = h = 30

    #Now just the two slabs left
    h = 5
    l = w = 30
    rs.currentLayer("SLABS")

    makeBox(x, y, z, l, w, h)
    z += 25
    makeBox(x, y, z, l, w, h)

#Setting it up to work if the file is run
if __name__ == "__main__":
    makeCagebox()