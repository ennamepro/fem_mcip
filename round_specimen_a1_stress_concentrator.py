#!/usr/bin/env python

### code aster analysis
### by MJB
### 2025-03-11

"""
Stress concentration analysis pipeline for round specimen.

Automated finite element analysis workflow for round specimens with circumferential
notches under axial loading. Performs parametric study varying notch radius and
specimen bar radius.

Key Parameters:
- Load force: 1000 N (uniform pressure on end face)
- Notch radius (undercut_radius): 1.5-12.0 mm (step 0.5 mm)
- Bar radius (bar_radius): 15.0-26.5 mm (step 0.5 mm)
- Specimen length (Xlength): 100 mm

Workflow:
1. Geometry generation (Salome Platform 9.14)
2. Mesh generation (Gmsh 4.13.1 - hexahedral elements)
3. FEA simulation (Code_Aster 17.0.8 via as_run)
4. Post-processing (ParaView 5.13.2)

External Dependencies:
- Salome, module Geometry
- Gmsh
- Code_Aster (as_run)
- ParaView

Input files (per parameter combination):
- export_pattern file for Code_Aster
- comm_pattern (round_specimen_a1_salome_pattern.comm) file for Code_Aster
- geometery (round_specimen_a1_salome_geom_pattern.py) file in Python (*.py) after modelling in Salome module Geometry
- paraview (round_specimen_a1_salome_pview_pattern.py) file in Python (*.py) for ParaView

Output files (per parameter combination):
- export (export_bar_radius_undercut_radius) files for Code_Aster
- comm (round_specimen_a1_salome_bar_radius_undercut_radius) files for Code_Aster
- geometery (round_specimen_a1_salome_geom_bar_radius_undercut_radius) files in Python (*.py) for Salome with -t -w1 parameters
- mesh result (round_specimen_a1_gmsh_bar_radius_undercut_radius) files in med and msh formats
- paraview (round_specimen_a1_salome_pview_radius_undercut_radius) files in Python (*.py) for ParaView with -t -w1 parameters

Usage:
    python round_specimen_a1_stress_concentrator_all_01.py
"""

# import time module
import time

# record start time
start_time = time.time()

# import other modules
import subprocess
import numpy as np
import gmsh

# model parameters

# number of decimals
nod = 3

# name of files and folders

file_ob1s = "round_specimen_a1_salome"
folder_breps = "round_specimen_a1_salome_breps/round_specimen_a1_salome"
folder_meds = "round_specimen_a1_salome_meds/round_specimen_a1_salome"
folder_comms = "round_specimen_a1_salome_comms/round_specimen_a1_salome"
folder_geoms = "round_specimen_a1_salome_geoms/round_specimen_a1_salome_geom"
folder_pviews = "round_specimen_a1_salome_pviews/round_specimen_a1_salome_pview"

# load force in N
load_force = 1000.00

# notch radius in mm, u_r
undercut_radius_min = 1.5
undercut_radius_max = 1.5 # max 12.0
undercut_radius_step = 0.5

# plate_width in mm, b_r
bar_radius_min = 15.0
bar_radius_max = 15.0 # max 26.5
bar_radius_step = 0.5

# functions

def modify_and_save_new_file(original_file_path, new_file_path, replacements):

    """
    Reads a text file, performs string replacements, and saves the modified content to a new file.

    This function is used to customize template files for FEA workflow by replacing placeholders
    with specific parameter values (e.g., radii).

    Args:
        original_file_path (str): Path to the input template file.
        new_file_path (str): Path where the modified file will be saved.
        replacements (dict): Dictionary mapping old strings to new strings for replacement.

    Returns:
        None.

    Raises:
        FileNotFoundError: If the original file does not exist.
        Exception: For any other errors during file operations.
    """

    try:
        # open the original file in read mode and read its content
        with open(original_file_path, 'r') as original_file:
            content = original_file.read()
        
        # replace multiple strings
        for old_string, new_string in replacements.items():
            content = content.replace(old_string, new_string)
        
        # open the new file in write mode and write the modified content
        with open(new_file_path, 'w') as new_file:
            new_file.write(content)
        print(f"Successfully replaced strings and saved to {new_file_path}.")
    
    except FileNotFoundError:
        print(f"The file {original_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def integer_part(float_num):

    """
    Extracts the integer part of a floating-point number.

    Used in filename generation for FEA simulations to prepare files with different bar and undercut radii.

    Args:
        float_num (float): Input floating-point number.

    Returns:
        int: The integer part of the input number.
    """

    integer_part = int(float_num)
    return integer_part

def fractional_part(float_num):

    """
    Extracts the fractional part of a floating-point number.

    Used in filename generation for FEA simulations to prepare files with different bar and undercut radii.

    Args:
        float_num (float): Input floating-point number.

    Returns:
        float: The fractional part of the input number (float_num - int(float_num)).
    """

    integer_part = int(float_num)
    fractional_part = float_num - integer_part
    return fractional_part

def gmsh_mesher(X_length, bar_radius, undercut_radius):

    """
    Generates a hexahedral mesh using Gmsh for a round specimen with circumferential notch.

    Imports BREP geometry, defines physical groups, applies size field for refinement near notch,
    generates 3D mesh, and saves in .msh and .med formats. Optimized for Code_Aster FEA.

    Args:
        X_length (float): Specimen length in mm.
        bar_radius (float): Bar radius in mm.
        undercut_radius (float): Notch (undercut) radius in mm.

    Returns:
        None.

    Note:
        Initializes and finalizes Gmsh; sets GUI options for visualization (edges and faces shown).
    """
    
    # initialize Gmsh
    gmsh.initialize()

    # add model to mesh
    gmsh.model.add(f"{file_ob1s}_gmsh_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}")

    # import BREP file and synchronise
    gmsh.model.occ.importShapes(f"{folder_breps}_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}.brep")
    
    # prepare model to mesh
    gmsh.model.geo.removeAllDuplicates()
    gmsh.model.occ.synchronize()

    # create physical groups for selected surfaces
    # add physical groups
    gmsh.model.addPhysicalGroup(2, [7, 14, 22, 28], tag=100)
    # set physical groups
    gmsh.model.setPhysicalName(2, 100, "X_min")

    gmsh.model.addPhysicalGroup(2, [4, 12 , 17, 24], tag=101)
    gmsh.model.setPhysicalName(2, 101, "X_max")

    gmsh.model.addPhysicalGroup(2, [5, 11], tag=102)
    gmsh.model.setPhysicalName(2, 102, "Y_0")

    gmsh.model.addPhysicalGroup(2, [3, 18], tag=103)
    gmsh.model.setPhysicalName(2, 103, "Z_0")

    # set values to refinement
    if undercut_radius < 5:
        thickness = 1
        VIn = undercut_radius + 0.25
    else:
        thickness = 2.5
        VIn = 5

    # create a Box field for mesh refinement
    box_field = gmsh.model.mesh.field.add("Box")
    gmsh.model.mesh.field.setNumber(box_field, "Thickness", thickness)
    gmsh.model.mesh.field.setNumber(box_field, "VIn", VIn)
    gmsh.model.mesh.field.setNumber(box_field, "VOut", 1e+22)
    gmsh.model.mesh.field.setNumber(box_field, "XMin", float(X_length)/2 - undercut_radius - thickness)
    gmsh.model.mesh.field.setNumber(box_field, "XMax", float(X_length)/2 + undercut_radius + thickness)
    gmsh.model.mesh.field.setNumber(box_field, "YMin", -bar_radius - 5)
    gmsh.model.mesh.field.setNumber(box_field, "YMax", bar_radius + 5)
    gmsh.model.mesh.field.setNumber(box_field, "ZMin", -bar_radius - 5)
    gmsh.model.mesh.field.setNumber(box_field, "ZMax", bar_radius + 5)

    # set the box field as the background field
    gmsh.model.mesh.field.setAsBackgroundMesh(box_field)

    # set subdivision algorithm for all-hexahedral mesh generation
    gmsh.option.setNumber("Mesh.SubdivisionAlgorithm", 2)

    # generate the mesh
    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(3)

    # save the mesh to a files
    gmsh.option.setNumber("Mesh.SaveAll", 1)
    gmsh.write(f"{folder_meds}_gmsh_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}.msh")
    gmsh.write(f"{folder_meds}_gmsh_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}.med")

    # gui show 2D faces parameters
    gmsh.option.setNumber("Mesh.SurfaceEdges", 1)   # show edges
    gmsh.option.setNumber("Mesh.SurfaceFaces", 1)   # show faces

    # run the gmsh gui - remove # below to the mesh
    # gmsh.fltk.run()

    # finalize Gmsh
    gmsh.finalize()

# export file parameters for Code_Aster
export_original_file_path = "export_pattern"
export_old_string = "_pattern"

# .comm file parameters
comm_original_file_path = "round_specimen_a1_salome_pattern.comm"
comm_old_string = "PRES=-X.XX"

# plate load in MPa
pres_rep = []

# geom and mesh parameters
X_length = X_length_pattern = "100"
bar_radius = bar_radius_min
undercut_radius = undercut_radius_min
geom_original_file_path = "round_specimen_a1_salome_geom_pattern.py"
geom_old_string = "_pattern"

# paraview file parameters
pview_original_file_path = "round_specimen_a1_salome_pview_pattern.py"
pview_old_string = "_pattern"

# mail loop
# prepare required data and text files
# run external application with prepared data files

while bar_radius <= bar_radius_max:
    while undercut_radius <= undercut_radius_max:         
        
        # calculate force as pressure
        pres_rep_loop = round(load_force / (np.pi * bar_radius**2), nod)
        pres_rep.append(pres_rep_loop)

        # set and prepare "export_pattern_bar_radius_undercut_radius" file for code_aster
        export_new_file_path = f"exports/export_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}"
        export_replacements = {export_old_string: f"_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}"}
        modify_and_save_new_file(export_original_file_path, export_new_file_path, export_replacements)
        
        # set and prepare "round_specimen_a1_salome_pattern_bar_radius_undercut_radius.comm" file for code_aster
        comm_new_file_path = f"{folder_comms}_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}.comm"
        comm_replacements = {comm_old_string: f"PRES=-{pres_rep_loop}"}
        modify_and_save_new_file(comm_original_file_path, comm_new_file_path, comm_replacements)
        
        # set and prepare round_specimen_a1_salome_geom_bar_radius_undercut_radius.py file for Salome Platform
        geom_new_file_path = f"{folder_geoms}_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}.py"
        geom_replacements = {"X_length_pattern": X_length_pattern,
                            "bar_radius_pattern": str(bar_radius),
                            "undercut_radius_pattern": str(undercut_radius),
                            "_pattern.brep": f"_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}.brep"}
        modify_and_save_new_file(geom_original_file_path, geom_new_file_path, geom_replacements)
        
        # run Salome Platform subprocess
        geom = subprocess.run(["../../../apps/salome_914/salome", "-t", "-w1", f"{folder_geoms}_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}.py"])

        # set and prepare round_specimen_a1_salome_pview_bar_radius_undercut_radius.py file for ParaView
        pview_new_file_path = f"{folder_pviews}_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}.py"
        pview_replacements = {pview_old_string : f"_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}"}
        modify_and_save_new_file(pview_original_file_path, pview_new_file_path, pview_replacements)
        
        # run Gmsh subprocess
        gmsh_mesher(X_length, bar_radius, undercut_radius)
        
        # run code_aster subprocess
        code_aster = subprocess.run(["as_run", f"exports/export_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}"])
        
        # run ParaView subprocess
        paraview = subprocess.run(["../../../apps/paraview_5132/bin/pvpython", f"{folder_pviews}_{integer_part(bar_radius)}_{str(fractional_part(bar_radius))[2:]}_{integer_part(undercut_radius)}_{str(fractional_part(undercut_radius))[2:]}.py"])
        
        undercut_radius += undercut_radius_step
    bar_radius += bar_radius_step
    undercut_radius = undercut_radius_min
    
# time calculation
end_time = time.time()
print(f'The time of execution of above program is: {end_time-start_time} s')
