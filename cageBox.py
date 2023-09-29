from boxmaker import *

#It's a function because reasons
def makeCagebox():
    x, y, z = 0, 0, 0
    l, w, h = 10, 10, 10

    #Layers are a part of the assignment
    outsideBoxes = rs.CreateColor(124, 150, 255)
    rs.AddLayer("BOXES", outsideBoxes)
    rs.CurrentLayer("BOXES")
    lineColor = rs.CreateColor(0, 0, 255)
    rs.AddLayer("CURVES", lineColor)
    slabColor = rs.CreateColor(118, 114, 217)
    rs.AddLayer("SLABS", slabColor)

    #Create 8 outer boxes
    while z <= 40:
        while x <= 40:
            while y <= 40:
                makeBox(x, y, z, l, w, h)
                y += 40
            x += 40
            y = 0
        z += 40
        x, y = 0, 0

    #Now create the lines in between the boxes. Why do i need so many lines :((((((
    rs.CurrentLayer("CURVES")
    x, y, z = 0, 0, 0
    l, w, h = 50, 50, 50
    offset1, offset2 = 50, 50

    for i in range(3):
        
        if i == 1:
            x, y, z = 10, 10, 0
        elif i == 2:
            x, y, z = 10, 0, 10
        else:
            x, y, z = 0, 0, 0

        zBuf = z
        while z <= offset2 + zBuf:
            yBuf = y
            while y <= offset1 + yBuf:
                rs.AddLine([x, y, z], [x+l, y, z])
                y += offset1
            y = yBuf
            z += offset2
            
        if i == 1:
            x, y, z = 10, 10, 0
        elif i == 2:
            x, y, z = 0, 10, 10
        else:
            x, y, z = 0, 0, 0

        zBuf = z
        while z <= offset2 + zBuf:
            xBuf = x
            while x <= offset1 + xBuf:
                rs.AddLine([x, y, z], [x, y+w, z])
                x += offset1
            x = xBuf
            z += offset2
        
        if i == 1:
            x, y, z = 0, 10, 10
        elif i == 2:
            x, y, z = 10, 0, 10
        else:
            x, y, z = 0, 0, 0

        xBuf = x
        while x <= offset2 + xBuf:
            yBuf = y
            while y <= offset1 + yBuf:
                rs.AddLine([x, y, z], [x, y, z+h])
                y += offset1
            y = yBuf
            x += offset2

        if i == 0:
            l, w, h = 30, 30, 30
            offset1 = 30
        if i == 1:
            offset1 = 50
            offset2 = 30

    #Now just the two slabs left
    l, w, h = 30, 30, 5
    x, y, z = 10, 10, 10
    rs.CurrentLayer("SLABS")

    makeBox(x, y, z, l, w, h)
    z += 25
    makeBox(x, y, z, l, w, h)

#Setting it up to work if the file is run
if __name__ == "__main__":
    makeCagebox()