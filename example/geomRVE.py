# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.2.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'D:/inputfiles/mehrskalen/newRVETests/UProfil/biegedrillfem3')

####################################################
##       Begin of NoteBook variables section      ##
####################################################
feapFileName = 'ifeap'

notebook.set("L", 5)
notebook.set("h", 10)
notebook.set("b", 10)
notebook.set("s", 0.6)
notebook.set("t", 1.2)
notebook.set("id", 0.5)
notebook.set("ex", "b*h")
notebook.set("x1", 0)
notebook.set("x2", "x1+s")
notebook.set("x3", "x1+b")
notebook.set("y1", 0)
notebook.set("y2", "y1+t")
notebook.set("y3", "y1+h-t")
notebook.set("y4", "y1+h")
notebook.set("ipos", "-id")
####################################################
##        End of NoteBook variables section       ##
####################################################
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
sk = geompy.Sketcher2D()
sk.addPoint(0.000000, 0.000000)
sk.addSegmentAbsolute('x3', 0.000000)
sk.addSegmentAbsolute('x3', 'y2')
sk.addSegmentAbsolute('x2', 'y2')
sk.addSegmentAbsolute('x2', 'y3')
sk.addSegmentAbsolute('x3', 'y3')
sk.addSegmentAbsolute('x3', 'y4')
sk.addSegmentAbsolute('x1', 'y4')
sk.close()
Sketch_1 = sk.wire(geomObj_1)
Face_1 = geompy.MakeFaceWires([Sketch_1], 1)
Rotation_1 = geompy.MakeRotation(Face_1, OX, 90*math.pi/180.0)
Rotation_2 = geompy.MakeRotation(Rotation_1, OZ, 90*math.pi/180.0)
geomObj_6 = geompy.MakeCDG(Rotation_2)
coor = geompy.PointCoordinates(geomObj_6)
Rotation_2 = geompy.MakeTranslation(Rotation_2, -coor[0], -coor[1], -coor[2])
Extrusion_1 = geompy.MakePrismVecH2Ways(Rotation_2, OX, "L")
Plane_1 = geompy.MakePlane(O, OX, "ex")
Translation_1 = geompy.MakeTranslation(Plane_1, "ipos", 0, 0)
Partition_1 = geompy.MakePartition([Extrusion_1, Plane_1, Translation_1], [], [], [], geompy.ShapeType["SOLID"], 0, [], 0)

Partition_1_vertex_127 = geompy.GetSubShape(Partition_1, [127])
h = notebook.get("L")*notebook.get("b")
Plane_2 = geompy.MakePlane(Partition_1_vertex_127, OZ, h)
Partition_1_vertex_125 = geompy.GetSubShape(Partition_1, [125])
Plane_3 = geompy.MakePlane(Partition_1_vertex_125, OZ, h)
Partition_2 = geompy.MakePartition([Partition_1, Plane_2, Plane_3], [], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
Partition_2_vertex_185 = geompy.GetSubShape(Partition_2, [185])
Plane_4 = geompy.MakePlane(Partition_2_vertex_185, OY, h)
Partition_3 = geompy.MakePartition([Partition_2, Plane_4], [], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
InterfaceLengthEdge = geompy.CreateGroup(Partition_3, geompy.ShapeType["EDGE"])
geompy.UnionIDs(InterfaceLengthEdge, [140])
LengthEdges = geompy.CreateGroup(Partition_3, geompy.ShapeType["EDGE"])
geompy.UnionIDs(LengthEdges, [13, 232])
sedges = geompy.CreateGroup(Partition_3, geompy.ShapeType["EDGE"])
geompy.UnionIDs(sedges, [230, 313, 242, 308])
InterfaceVol = geompy.CreateGroup(Partition_3, geompy.ShapeType["SOLID"])
geompy.UnionIDs(InterfaceVol, [132, 156, 173, 190, 212])
VolGroup = geompy.CreateGroup(Partition_3, geompy.ShapeType["SOLID"])
geompy.UnionIDs(VolGroup, [108, 2, 224, 248, 265, 282, 304, 36, 60, 84])
Interface2D = geompy.CreateGroup(Partition_3, geompy.ShapeType["FACE"])
geompy.UnionIDs(Interface2D, [146, 168, 188, 210, 222])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sketch_1, 'Sketch_1' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Rotation_2, 'Rotation_2' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( Plane_1, 'Plane_1' )
geompy.addToStudy( Partition_1, 'Partition_1' )

geompy.addToStudy( Partition_3, 'Partition_3' )
geompy.addToStudyInFather( Partition_3, InterfaceLengthEdge, 'InterfaceLengthEdge' )
geompy.addToStudyInFather( Partition_3, LengthEdges, 'LengthEdges' )
geompy.addToStudyInFather( Partition_3, sedges, 'sedges' )
geompy.addToStudyInFather( Partition_3, InterfaceVol, 'InterfaceVol' )
geompy.addToStudyInFather( Partition_3, VolGroup, 'VolGroup' )
geompy.addToStudyInFather( Partition_3, Interface2D, 'Interface2D' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Partition_3)
Regular_1D = Mesh_1.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(2)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)
Regular_1D_1 = Mesh_1.Segment(geom=InterfaceLengthEdge)
Number_of_Segments_2 = Regular_1D_1.NumberOfSegments(1)
Regular_1D_2 = Mesh_1.Segment(geom=sedges)
Number_of_Segments_3 = Regular_1D_2.NumberOfSegments(2)
Propagation_of_1D_Hyp = Regular_1D_1.Propagation()
status = Mesh_1.AddHypothesis(Propagation_of_1D_Hyp,sedges)
nodeID = Mesh_1.AddNode( 0, 0, 0 )
nodeID = Mesh_1.AddNode( 0, 0, 0 )
nodeID = Mesh_1.AddNode( 0, 0, 0 )
nodeID = Mesh_1.AddNode( 0, 0, 0 )
nodeID = Mesh_1.AddNode( 0, "b", 0 )
nodeID = Mesh_1.AddNode( 0, "b", 0 )
nodeID = Mesh_1.AddNode( 0, 0, 0 )
nodeID = Mesh_1.AddNode( 0, 0, 0 )
isDone = Mesh_1.Compute()
Mesh_1.ConvertToQuadratic(0, Mesh_1,True)
Interface3D = Mesh_1.GroupOnGeom(InterfaceVol,'Interface3D',SMESH.VOLUME)
Volume = Mesh_1.GroupOnGeom(VolGroup,'Volume',SMESH.VOLUME)
Interface2D_1 = Mesh_1.GroupOnGeom(Interface2D,'Interface2D',SMESH.FACE)
Interface3D2 = Mesh_1.DoubleElements( Interface3D, 'DoubleElements')
Interface3D2.SetName( 'Interface3D2' )
Volume2 = Mesh_1.DoubleElements( Volume, 'DoubleElements')
Volume2.SetName( 'Volume2' )
Interface3D3 = Mesh_1.DoubleElements( Interface3D, 'DoubleElements')
Interface3D3.SetName( 'Interface3D3' )
Sub_mesh_1 = Regular_1D_1.GetSubMesh()
Sub_mesh_2 = Regular_1D_2.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(Number_of_Segments_3, 'Number of Segments_3')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Interface2D_1, 'Interface2D')
smesh.SetName(Propagation_of_1D_Hyp, 'Propagation of 1D Hyp. on Opposite Edges_1')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
smesh.SetName(Interface3D3, 'Interface3D3')
smesh.SetName(Volume2, 'Volume2')
smesh.SetName(Interface3D2, 'Interface3D2')
smesh.SetName(Volume, 'Volume')
smesh.SetName(Interface3D, 'Interface3D')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')



# feap Part
import os, inspect
import feap
import mate

fobj = feap.feap()

fobj.setNdf(3)
fobj.setNdm(3)
fobj.setNumMat(4)


fobj.addNodesSalome(Mesh_1)
fobj.addElemsSalome(Mesh_1,Volume,SMESH.EntityType)
fobj.addElemsSalome(Mesh_1,Interface3D,SMESH.EntityType)
fobj.addElemsSalome(Mesh_1,Volume2,SMESH.EntityType)
fobj.addElemsSalome(Mesh_1,Interface3D2,SMESH.EntityType)
fobj.addElemsSalome(Mesh_1,Interface3D3,SMESH.EntityType)
fobj.addElemsSalome(Mesh_1,Interface2D_1,SMESH.EntityType)

fobj.reorder(Volume,'mult')
fobj.reorder(Interface3D,'mult')
fobj.reorder(Volume2,'mult')
fobj.reorder(Interface3D2,'mult')
fobj.reorder(Interface3D3,'mult')
fobj.reorder(Interface2D_1,'mult')


fobj.setMatGroupSalome(Volume,1)
fobj.setMatGroupSalome(Interface3D,1)
fobj.setMatGroupSalome(Volume2,2)
fobj.setMatGroupSalome(Interface3D2,2)
fobj.setMatGroupSalome(Interface3D3,3)
fobj.setMatGroupSalome(Interface2D_1,4)

fobj.addNodesToElementGroupSalome(Interface3D2,[1, 2])
fobj.addNodesToElementGroupSalome(Volume2,[1, 2])
fobj.addNodesToElementGroupSalome(Interface3D3,[3, 4])
fobj.addNodesToElementGroupSalome(Interface2D_1,[5, 6, 7, 8])

fobj.setSolver([4])

fobj.addCons("e",21000)
fobj.addCons("v",0.3)

h=mate.mate()
h.setNumEl(1,21)
h.setLine(1,[1,1,0,0,5,5,1])
h.setLine(2,[0,0,0])
h.setLine(3,["e","v",0])
fobj.addMate(h)

h=mate.mate()
h.setNumEl(2,23)
h.setLine(1,[1,notebook.get("L"),1,0,0,5,5,1])
h.setLine(2,["e","v",0])
fobj.addMate(h)

h=mate.mate()
h.setNumEl(3,24)
h.setLine(1,[1,0,0,0,5,5,1])
h.setLine(2,["e","v",0])
fobj.addMate(h)

h=mate.mate()
h.setNumEl(4,98)
fobj.addMate(h)

fobj.addBoun(3,[1,1,1])
fobj.addBoun(4,[0,0,1])
fobj.addBoun(6,[0,1,1])
fobj.addBoun(7,[1,1,1])
fobj.addBoun(8,[1,1,1])

fobj.addMacroLine('link')
temp = '4,1,' + str(-notebook.get('L')) + ',' + str(notebook.get('L'))
fobj.addMacroLine(temp)
fobj.addMacroLine('')
fobj.addMacroLine('macr')
fobj.addMacroLine('prop')
fobj.addMacroLine('end')
fobj.addMacroLine('')
fobj.addMacroLine('inte')
fobj.addMacroLine('stop')


fobj.addMacroLine('')
fobj.addMacroLine('')
fobj.addMacroLine('epsq')
fobj.addMacroLine('3,6,4,1,1')
fobj.addMacroLine('0,0.0,0.10,0.,0.0,')


fdir = os.path.dirname(inspect.getfile(inspect.currentframe()))
fileName = os.path.join( fdir, feapFileName )
fileObj = open(fileName, "w")
fobj.toFile(fileObj)
fileObj.close()


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
