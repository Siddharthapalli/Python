#PROGRAM TO EXTRACT INITIAL & FINAL COORDINATES AFTER LOADING AND WRITING THE OUTPUT TO A CSV FILE
import os, sys
from abaqus import *
from abaqusConstants import *
import visualization
#Defining a viewport
myViewport = session.Viewport(name='Superposition example')
#Open odb
myOdb = visualization.openOdb(path='E:\ABAQUS_FILES\check\Job__2LOADS.odb')
#Odb to be displayed in the predefined viewport
myViewport.setValues(displayedObject=myOdb)
#defining Steps & Frames
firstStep = myOdb.steps['Step-1']
frame1 = firstStep.frames[0]
frame2 = firstStep.frames[-1]
#Defining the particular nodeset from which you need the result
RESULTNODES = myOdb.rootAssembly.nodeSets['RESULT']
#Defining the required Output COORD in this case
displacement=frame1.fieldOutputs['COORD']
#Calling Desired output of required nodeset
centerDisplacement = displacement.getSubset(region=RESULTNODES)
centerValues = centerDisplacement.values
displacement=frame2.fieldOutputs['COORD']
centerDisplacement = displacement.getSubset(region=RESULTNODES)
centerValues1 = centerDisplacement.values
# coding: utf-8
#Creating a csv file to which result is exported
myoutfile = open('Initial_Final_Coordinates.csv','w+')
myoutfile.write("InitialCoordinates - - - FinalCoordinates\n")
myoutfile.write("Node ")
myoutfile.write("x ")
myoutfile.write("y ")
myoutfile.write("z ")
myoutfile.write("x' ")
myoutfile.write("y' ")
myoutfile.write("z'\n")
#for all the nodes in datasets output will be extracted node id,x,y,z Initial final coordinates
for i,j in zip(centerValues,centerValues1):
  print 'Node label =', i.nodeLabel
  myoutfile.write(str(i.nodeLabel))
  myoutfile.write(" ")
  print 'x disp =', i.data[0]
  myoutfile.write(str(i.data[0]))
  myoutfile.write(" ")
  print 'y disp =', i.data[1]
  myoutfile.write(str(i.data[1]))
  myoutfile.write(" ")
  print 'z disp =', i.data[2]
  myoutfile.write(str(i.data[2]))
  myoutfile.write(" ")
  print 'x disp =', j.data[0]
  myoutfile.write(str(j.data[0]))
  myoutfile.write(" ")
  print 'y disp =', j.data[1]
  myoutfile.write(str(j.data[1]))
  myoutfile.write(" ")
  print 'z disp =', j.data[2]
  myoutfile.write(str(j.data[2]))
  myoutfile.write("\n")
myoutfile.close()
