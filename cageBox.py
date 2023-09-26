from boxmaker import *

def makeCagebox():
    x = y = z = 0
    l = w = h = 10
    lines  = []
    i = 0
    outsideBoxes = rs.createColor(124, 150, 255)
    rs.addLayer("BOXES", outsideBoxes)
    rs.currentLayer("BOXES")
    rs.deleteLayer(Default)
    lines = rs.createColor(106, 255, 158)
    rs.addLayer("CURVES", lines)

    while z <= 40:
        while x <= 40:
            while y <= 40:
                rs.currentLayer("BOXES")
                makeBox(x, y, z, l, w, h)
                y += 40
            rs.currentLayer("CURVES")
            lines[i] = rs.addLine([[l, ], []])
            i += 1
            x += 40
            y = 0
        z += 40
        x = 0
        y = 0

makeCagebox()