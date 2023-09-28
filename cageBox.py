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
        x = y = 0

    #Now create the lines in between the boxes. Why do i need so many lines :((((((
    rs.currentlayer("CURVES")
    x = y = z = 0
    l = w = h = 50
    offset1 = offset2 = 50

    for j in range(2):
        while z <= offset2 + z:
            while y <= offset1 + y:
                lines[i] = rs.newLine([[x, y, z], [x+l, y, z]])
                i =+ 1
                y += offset1
            y = 0
            z += offset2
            
        if j == 1:
            x, y, z = 10, 10, 0
        else:
            x = y = z = 0

        while z <= offset2 + z:
            while x <= offset1 + x:
                lines[i] = rs.newLine([[x, y, z], [x, y+w, z]])
                i =+ 1
                x += offset1
            x = 0
            z += offset2
        
        if j == 1:
            x, y, z = 10, 0, 10
        else:
            x = y = z = 0

        while x <= offset2 + x:
            while y <= offset1 + y:
                lines[i] = rs.newLine([[x, y, z], [x, y, z+h]])
                i =+ 1
                y += offset1
            y = 0
            x += offset2
        
        if j == 1:
            x, y, z = 10, 10, 0
        else:
            x = y = z = 0

        l = w = h = 30
        offset1 = 30

    #Now just the two slabs left
    l, w, h = 30, 30, 5
    rs.currentLayer("SLABS")

    makeBox(x, y, z, l, w, h)
    z += 25
    makeBox(x, y, z, l, w, h)

#Setting it up to work if the file is run
if __name__ == "__main__":
    makeCagebox()