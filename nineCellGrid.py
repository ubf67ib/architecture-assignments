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
    lines[0] = rs.NewLine((x, y, z+h), (x+l, y, z+h))
    lines[1] = rs.NewLine((x+l, y, z+h), (x+l, y+w, z+h))
    lines[2] = rs.NewLine((x+l, y, z+h), (x+l, y, z))

    for i in lines:
        points[i] = rs.DivideCurve(lines[i], 18, create_points=True, return_points=True)
    
    #TODO: make this user imputted
    splitNumbers = [[6, 12], [4, 10], [8, 14]]
    for i in splitNumbers[0]:
        planes[0][i] = rs.PlaneFromNormal(lines[0][i], [1, 0, 0])
    for i in splitNumbers[1]
        planes[0][i] = rs.PlaneFromNormal(lines[0][i], [0, 1, 0])

if __name__ == "__main__":
    makeBox()