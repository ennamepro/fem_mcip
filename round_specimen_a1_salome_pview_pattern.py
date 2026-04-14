# trace generated using paraview version 5.13.2
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 13

# import is library
import os

# set current directory
current_dir = os.getcwd()

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# load plugin
LoadPlugin('MEDReader', remote=False, ns=globals())

# create a new 'MED Reader'
round_specimen_a1_salome_rmed = MEDReader(registrationName='round_specimen_a1_salome_pattern.rmed', FileNames=os.path.join(current_dir, 'round_specimen_a1_salome_rmeds', 'round_specimen_a1_salome_pattern.rmed'))

# Properties modified on round_specimen_a1_salome_rmed
round_specimen_a1_salome_rmed.FieldsStatus = ['TS0/00000001/ComSup0/reslin__DEPL@@][@@P1', 'TS0/00000001/ComSup0/reslin__SIEF_ELGA@@][@@GAUSS', 'TS0/00000001/ComSup0/reslin__SIEQ_NOEU@@][@@P1', 'TS0/00000001/ComSup0/reslin__SIGM_NOEU@@][@@P1']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
round_specimen_a1_salome_rmedDisplay = Show(round_specimen_a1_salome_rmed, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
round_specimen_a1_salome_rmedDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(True, 0.9)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

renderView1.ApplyIsometricView()

# reset view to fit data
renderView1.ResetCamera(True, 0.9)

# set scalar coloring
ColorBy(round_specimen_a1_salome_rmedDisplay, ('POINTS', 'reslin__SIEQ_NOEU', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
round_specimen_a1_salome_rmedDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
round_specimen_a1_salome_rmedDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'reslin__SIEQ_NOEU'
reslin__SIEQ_NOEULUT = GetColorTransferFunction('reslin__SIEQ_NOEU')

# get opacity transfer function/opacity map for 'reslin__SIEQ_NOEU'
reslin__SIEQ_NOEUPWF = GetOpacityTransferFunction('reslin__SIEQ_NOEU')

# get 2D transfer function for 'reslin__SIEQ_NOEU'
reslin__SIEQ_NOEUTF2D = GetTransferFunction2D('reslin__SIEQ_NOEU')

# set scalar coloring
ColorBy(round_specimen_a1_salome_rmedDisplay, ('POINTS', 'reslin__SIEQ_NOEU', 'TRIAX'))

# rescale color and/or opacity maps used to exactly fit the current data range
round_specimen_a1_salome_rmedDisplay.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(reslin__SIEQ_NOEULUT, round_specimen_a1_salome_rmedDisplay)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
reslin__SIEQ_NOEULUT.ApplyPreset('Rainbow Uniform', True)

renderView1.ApplyIsometricView()

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# Properties modified on renderView1
renderView1.CenterOfRotation = [50.0, 25.0, 2.5]
renderView1.CameraPosition = [185.0, -145.0, 100.0]
renderView1.CameraFocalPoint = [50.000000000000014, 24.999999999999957, 2.5000000000000058]
renderView1.CameraViewUp = [-0.2467586224231631, 0.31223389342493424, 0.9173985927918844]
renderView1.CameraParallelScale = 55.95757321399848

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 100.0, -26.5, 26.5, -26.5, 26.5, True, 0.9)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(3001, 1732)

# current camera placement for renderView1
renderView1.CameraPosition = [186.95950497726298, -172.46752478618293, 98.91519803913437]
renderView1.CameraFocalPoint = [50.0, 0.0, 0.0]
renderView1.CameraViewUp = [-0.2467586224231631, 0.31223389342493424, 0.9173985927918844]
renderView1.CameraViewAngle = 27.540415704387993
renderView1.CameraParallelScale = 62.48599843164867

# save screenshot
SaveScreenshot(filename=os.path.join(current_dir, 'round_specimen_a1_salome_pngs', 'round_specimen_a1_salome_pattern.png'), viewOrLayout=renderView1, location=16, ImageResolution=[3001, 1732],
    TransparentBackground=1, 
    # PNG options
    CompressionLevel='9')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(3001, 1732)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [186.95950497726298, -172.46752478618293, 98.91519803913437]
renderView1.CameraFocalPoint = [50.0, 0.0, 0.0]
renderView1.CameraViewUp = [-0.2467586224231631, 0.31223389342493424, 0.9173985927918844]
renderView1.CameraViewAngle = 27.540415704387993
renderView1.CameraParallelScale = 62.48599843164867


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
