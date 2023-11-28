import rhinoscriptsyntax as rs
from boxmaker import *

#TODO: Make this user inputted
lines = [[0.3, 0.6], [0.4, 0.8], [0.2, 0.7]]
x, y, z = 0, 0, 0

#Puteverything on a new layer
rs.CurrentLayer = rs.AddLayer()

#Just make the boxes
for i in lines[0]:
    makeBox(x+i*9-3/32, y, z, 3/16, 9, 9)
for i in lines[1]:
    makeBox(x, y+i*9-3/32, z, 9, 3/16, 9)
for i in lines[2]:
    makeBox(x, y, z+i*9-3/32, 9, 9, 3/16)