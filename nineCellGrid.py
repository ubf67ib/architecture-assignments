import rhinoscriptsyntax as rs
from boxmaker import *

#There's no split by plane, so this function will be useful later
def planeToBrep(plane):


#I can't be bothered to make it object oriented
def makeBox():
    x, y, z = 0, 0, 0
    l, w, h = 9, 9, 9

    #Setup layering so it doesn't care about preexisting stuff
    layer = rs.AddLayer()
    if rs.currentlayer() != layer:
        rs.CurrentLayer(layer)

    makeBox(x, y, z, l, w, h)
    lines = {}
    lines[0] = rs.NewLine((x, y, z+h), (x+l, y, z+h))
    lines[1] = rs.NewLine((x+l, y, z+h), (x+l, y+w, z+h))
    lines[2] = rs.NewLine((x+l, y, z+h), (x+l, y, z))

    points = {}
    for i in lines:
        points[i] = rs.DivideCurve(lines[i], 18, create_points=True, return_points=True)
    
    #TODO: make this user imputted
    splitNumbers = [[6, 12], [4, 10], [8, 14]]

    pl
    for i in splitNumbers[0]:
        planes[0][i] = rs.PlaneFromNormal(lines[0][i], [1, 0, 0])
    for i in splitNumbers[1]:
        planes[1][i] = rs.PlaneFromNormal(lines[1][i], [0, 1, 0])
    for i in splitNumbers[2]:
        planes[2][i] = rs.PlaneFromNormal(lines[2][i], [0, 0, 1])

    #Now make the planes into breps because you can't split by plane
    i = 0
    while i < len(planes):
        for j in planes[i]:
            planeSrfs[i][]
        i += 1

if __name__ == "__main__":
    makeBox()