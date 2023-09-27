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
    lineColor = rs.createColor(106, 255, 158)
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

    #Now create the lines in between the boxes
    rs.currentlayer("CURVES")
    x = y = z = 0
    l = w = h = 50

    #Why are there so many lines I need :((((((
    while z <= 40:
        while y <= 40:
            lines[i] = rs.newLine([[x, y, z], [x+l, y, z]])
            i =+ 1
            y += 30
        y = 0
        z += 30
    x = y = z = 0

    while z <= 40:
        while x <= 40:
            lines[i] = rs.newLine([[x, y, z], [x, y+w, z]])
            i =+ 1
            x += 30
        x = 0
        z += 30
    x = y = z = 0

    while x <= 40:
        while y <= 40:
            lines[i] = rs.newLine([[x, y, z], [x, y, z+h]])
            i =+ 1
            y += 30
        y = 0
        x += 30
    x = y = z = 0

    #Now just the two slabs left
    h = 5
    rs.currentLayer("SLABS")

    makeBox(x, y, z, l, w, h)
    z += 25
    makeBox(x, y, z, l, w, h)

#Setting it up to work if the file is run
if __name__ == "__main__":
    makeCagebox()