#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.14.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

# set variables

X_length = X_length_pattern
bar_radius = bar_radius_pattern
undercut_radius = undercut_radius_pattern

geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Cylinder_1 = geompy.MakeCylinder(O, OX, bar_radius, X_length)
Disk_1 = geompy.MakeDiskR(undercut_radius, 3)
Translation_1 = geompy.MakeTranslation(Disk_1, X_length/2, 0, bar_radius)
Revolution_1 = geompy.MakeRevolution(Translation_1, OX, 360*math.pi/180.0)
Cut_1 = geompy.MakeCutList(Cylinder_1, [Revolution_1], True)
Plane_Y_0 = geompy.MakePlane(O, OY, 250)
Plane_Z_0 = geompy.MakePlane(O, OZ, 250)
Partition_1 = geompy.MakePartition([Cut_1], [Plane_Y_0, Plane_Z_0], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
Compound_1 = geompy.MakeCompound([Partition_1])
X_min = geompy.CreateGroup(Compound_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(X_min, [113, 78, 46, 132])
X_max = geompy.CreateGroup(Compound_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(X_max, [121, 92, 33, 73])
Y_0 = geompy.CreateGroup(Compound_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Y_0, [65, 36])
Z_0 = geompy.CreateGroup(Compound_1, geompy.ShapeType["FACE"])
geompy.ExportBREP(Compound_1, "../round_specimen_a1_salome_breps/round_specimen_a1_salome_pattern.brep")
geompy.UnionIDs(Z_0, [95, 22])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudy( Disk_1, 'Disk_1' )
geompy.addToStudy( Translation_1, 'Translation_1' )
geompy.addToStudy( Revolution_1, 'Revolution_1' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudy( Plane_Y_0, 'Plane_Y_0' )
geompy.addToStudy( Plane_Z_0, 'Plane_Z_0' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudy( Compound_1, 'Compound_1' )
geompy.addToStudyInFather( Compound_1, Y_0, 'Y_0' )
geompy.addToStudyInFather( Compound_1, X_max, 'X_max' )
geompy.addToStudyInFather( Compound_1, Z_0, 'Z_0' )
geompy.addToStudyInFather( Compound_1, X_min, 'X_min' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
