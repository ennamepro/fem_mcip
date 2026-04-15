# fem_mcip
FEM multiple calculation in a pipeline (fem_mcip) using open‑source tools / Multiple FEM analyses using open‑source tools

by MJB
2026-03-21

Note: If you are only interested in running the fem_mcip calculations, go to Appendix A.  
Note: bash ... means that you should use the bash shell.  
Note: python ... means a part of a program written in the Python language.

### ### ### ### ###
1. Definition of task and objective
### ### ### ### ###

1.1. Define the task and objective of the simulation.  
1.2. Define the basis for the actions, including verification and validation of the results.  
1.3. Prepare and analyse the sample data.

### ### ### ### ###
2. Resources
### ### ### ### ###

Note: The resource creation scheme is shown in modelling_process_diagram.pdf.

2.1. Install the required operating system, e.g. Kubuntu.  
2.1.1. Kubuntu: https://cdimage.ubuntu.com/kubuntu/releases/24.04.4/release/

Note: Version used: 24.04.4.

2.2. Install the Miniconda environment: https://repo.anaconda.com/miniconda/

Note: Version used: py312_24.7.1-0.  
Note: A detailed description of the installation and configuration of the Miniconda environment is provided in Appendix B.

2.3. Install FreeCAD: https://www.freecad.org/downloads.php?lang=en

Note: Version used: 1.0.  
Note: It is recommended to use version 1.1 in the AppImage package: https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.0  
Note: It is recommended to install the package in a directory, e.g. home/user/apps/freecad_11 – instead of the string "user", use your own data, e.g. "john_smith".

2.4. Install Salome Platform: https://www.salome-platform.org/?page_id=2430

Note: Version used: 9.14.0, Linux Universal.  
Note: It is recommended to install it in a directory, e.g. home/user/apps/salome_914 – instead of the string "user", use your own data, e.g. "john_smith".

2.5. Install Gmsh: https://gmsh.info/bin/Linux/gmsh-4.13.1-Linux64.tgz

Note: Version used: 4.13.1.  
Note: It is recommended to install it in a directory, e.g. home/user/apps/gmsh_4131 – instead of the string "user", use your own data, e.g. "john_smith".  
Note: For multiple analysis, the gmsh 4.13.1 library from the pip repository was used, see Appendix B.

2.6. Install Salome Meca: https://code-aster.org/spip.php?article303

Note: Version used: salome_meca-lgpl-2024.1.0-1-20240327.  
Note: It is recommended to install it in a directory, e.g. home/user/apps/salome_meca_2k14 – instead of the string "user", use your own data, e.g. "john_smith".  
Note: For multiple analysis, the code_aster 17.0.1 library from the conda-forge repository was used, see Appendix B.

2.7. Install ParaView: https://www.paraview.org/download/

Note: Version used: 5.13.2.  
Note: It is recommended to install it in a directory, e.g. home/user/apps/paraview_5132 – instead of the string "user", use your own data, e.g. "john_smith".

2.8. Create a main directory, e.g. fem_mcip, for the purposes of the simulation. Free disk space must be checked.

Note: It is recommended to place it in a directory, e.g. home/user/analyses/fem_mcip – instead of the string "user", use your own data, e.g. "john_smith".

2.9. Install git. Installation of the system version available directly from the git resources was chosen.  
2.9.1. Add the git repository:

```bash
sudo add-apt-repository ppa:git-core/ppa
```

2.9.2. Update the apt repositories:

```bash
sudo apt update
```

2.9.3. Install git with the command:

```bash
sudo apt install git
```

2.9.4. Download resources from GitHub.

```bash
git clone https://github.com/ennamepro/fem_mcip.git
```

2.10. If you do not want to use Git, you can manually create all the required directories, e.g. with the command `md base-stage1s`.  
2.10.1. base-stage1s  
2.10.2. exports  
2.10.3. round_specimen_a1_salome_breps  
2.10.4. round_specimen_a1_salome_comms  
2.10.5. round_specimen_a1_salome_geoms  
2.10.6. round_specimen_a1_salome_meds  
2.10.7. round_specimen_a1_salome_pngs  
2.10.8. round_specimen_a1_salome_pviews  
2.10.9. round_specimen_a1_salome_rmeds  
2.10.10. round_specimen_a1_salome_txts

Note: An example structure of the main directory is included in the GitHub repository mentioned above.  
Note: Remember to copy all files from the repository to a directory on your computer.

### ### ### ### ###
3. Preparation
### ### ### ### ###

Note: This section describes the steps carried out during simulation preparation. If you want to use only the downloaded resources, go to section 3.9.

3.1. Model the sample variability in 3D using FreeCAD. Save the sample files in the directory: fcstds.  
3.1.1. As variables in the model of the round specimen with a semicircular notch, the values `bar_radius` and `undercut_radius` were chosen.

Note: Example views of the samples are shown in round_specimen_a1_salome_all.pdf.

3.2. Model the specimen in the Geometry module of Salome Platform. You can use many training materials, e.g. https://docs.salome-platform.org/latest/main/index.html  
3.2.1. Remember to create groups (physical groups), as in the template round_specimen_a1_salome_geom_pattern.py.  
3.2.2. Save the model in *.brep format in the directory round_specimen_a1_salome_breps.  
3.2.3. Save the model as Dump Study under the chosen name round_specimen_a1_salome_geom_pattern.py in the main directory elasf_fc.

3.3. Open the file round_specimen_a1_salome_geom_pattern.py in an editor, e.g. Kate.  
3.3.1. In the file, prepare variables for the current parameters, see the file round_specimen_a1_salome_geom_pattern.py:  
3.3.1.1. `X_length = X_length_pattern` (not required)  
3.3.1.2. `bar_radius = bar_radius_pattern`  
3.3.1.3. `undercut_radius = undercut_radius_pattern`  
3.3.2. Replace the current variables, e.g. "15" as the bar radius, with `bar_radius`. In the file round_specimen_a1_salome_geom_pattern.py, in places outside the definitions, all current parameters have already been replaced, e.g. with `bar_radius`.  
3.3.4. Save the file round_specimen_a1_salome_geom_pattern.py in the main directory.

3.4. Generate a mesh using Gmsh. You can use many training materials, e.g. https://gmsh.info/#Documentation  
3.4.1. Remember to define Physical Groups. In the file round_specimen_a1_stress_concentrator_all.py, physical groups are defined in the function `gmsh_mesher`.  
3.4.2. Save the model in *.geo format in the main directory. This will make it possible to define the meshing method in the function `gmsh_mesher`. Use the methods (parameters given as examples):  
`gmsh.model.addPhysicalGroup(2, [3, 18], tag=103)`,  
`gmsh.model.setPhysicalName(2, 103, "Z_0")`.

3.5. Prepare the analysis in Salome Meca using the previously prepared mesh. You can use training materials, e.g. https://code-aster.org/spip.php?rubrique68  
3.5.1. You can use the file round_specimen_a1_salome_pattern.comm to prepare the analysis.  
3.5.2. After verifying the analysis, use the export file to prepare a template, the file export_pattern. The export file should be in the directory created by Salome Meca – `project_name_Files/RunCase_1/Result-Stage_1`.  
3.5.3. The export_pattern file used is located in the main directory. It can be used to compare with the export file obtained from the FEM analysis. In the export_pattern file, the paths must be changed – they are provided in the export file. The files and their parameters must remain as below:  
3.5.3.1. `F comm /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/round_specimen_a1_salome_comms/round_specimen_a1_salome_pattern.comm D  1`  
3.5.3.2. `F libr /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/round_specimen_a1_salome_meds/round_specimen_a1_salome_pattern_gmsh.med D  20`  
3.5.3.3. `F libr /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/round_specimen_a1_salome_rmeds/round_specimen_a1_salome_pattern.rmed R  80`  
3.5.3.4. `F libr /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/round_specimen_a1_salome_txts/round_specimen_a1_salome_pattern.txt R  8`  
3.5.3.5. `F mess /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/messages/message_pattern R  6`  
3.5.3.6. `R base /home/user/data/analyses/fem_mcip/round_specimen_a1_salome/base-stage1s/base-stage1_pattern R  0`

Note: Instead of the string "user", use your own data, e.g. "john_smith".

3.6. Prepare a comm file based on which Code_Aster will perform the FEM analyses. You can use the template round_specimen_a1_salome_pattern.comm. In it, a string `PRES=-X.XX` has been prepared, which will be changed to a numerical value of the pressure that constitutes the tensile force in the bar. The remaining parameters of your simulation are contained in the comm file in the directory `project_name_Files/RunCase_1/Result-Stage_1`.

Note: Example view of the boundary conditions is shown in round_specimen_a1_salome_bc.pdf.

3.6.1. Note that the analysis uses reduced HMH stresses (Huber, Mises, Hencky), principal stresses 1, 2, 3, and the stress state triaxiality. Therefore, in the results the following were marked: `NOM_CMP=('VMIS', 'PRIN_1', 'PRIN_2', 'PRIN_3', 'TRIAX')`. In other works, you can change the recorded quantities.

3.7. Using ParaView, you can prepare a visualization of the calculation results. For this purpose, use the rmed file from the FEM calculations.  
3.7.1. In ParaView, call the command: Tools/Start Trace.  
3.7.2. In ParaView, load the rmed file. Remember that in Tools/Manage Plugins you must select MEDReader with Auto Load. In this case, the rmed file translator will be started when ParaView launches.  
3.7.3. Set all view parameters, displayed fields, e.g. HMH, etc. Remember that during the sequence of calculations, the specimens will differ in size. This must be anticipated.  
3.7.4. After preparing the desired visualization in ParaView, use the command: Tools/Stop Trace. A window with a Python script will appear. Remember to add to it:

```python
LoadPlugin('MEDReader', remote=False, ns=globals())
```

this will add the requirement to load the MED format translator. This is necessary because the Tools/Stop Trace command generates a Python script, but does not add the requirement to load the MEDReader plugin.

3.7.5. Visualization of results in ParaView requires preparing an appropriate template. For this purpose, you can use the file round_specimen_a1_salome_pview_pattern.py.

3.8. Activate the conda environment, e.g. py311.

```bash
conda activate py311
```

3.9. Start the Spyder application with the file round_specimen_a1_stress_concentrator.py loaded:

```bash
spyder round_specimen_a1_stress_concentrator.py
```

3.9.1. Prepare counters which are the radii of the notch and the specimen, and the iteration steps, e.g.:

```python
undercut_radius_min = 1.5
undercut_radius_max = 1.5 # max 12.0
undercut_radius_step = 0.5

bar_radius_min = 15.0
bar_radius_max = 15.0 # max 26.5
bar_radius_step = 0.5
```

3.9.2. Due to possible errors, in the counters:

```python
undercut_radius_max = 1.5 # max 12.0
bar_radius_max = 15.0 # max 26.5
```

values were adopted that will cause only a single iteration to be performed.

3.9.3. Place the prepared counters in the run file round_specimen_a1_stress_concentrator.py.  
3.10. Call the Run command (F5).  
3.10.1. If no errors appear, change the counter parameters to:

```python
undercut_radius_max = 12.0
bar_radius_max = 26.5
```

3.11. Call the Run command (F5), wait for the program to complete – this may take several hours.

### ### ### ### ###
4. Program operation
### ### ### ### ###

Note: The calculation execution scheme is shown in process_calculation_diagram.pdf.

4.1. Preparation of instructions for loop execution.  
4.2. Use of a while loop in the program from the min value to the max value.  
4.3. Calculation of the tensile force in the specimen. In the program, the force was distributed over the lateral surface of the specimen.
4.4. Preparation of the export file according to the export_pattern template for the next specimen.  
4.5. Preparation of the comm file according to the round_specimen_a1_salome_pattern.comm template for the next specimen.  
4.6. Preparation of the geometry file for Salome Platform according to the round_specimen_a1_salome_geom_pattern.py template for the next specimen.  
4.7. Preparation of the pview file for ParaView according to the round_specimen_a1_salome_pview_pattern.py template for the next specimen.  
4.8. Launch of the Salome Platform application with a parameter being the name of the script that creates the geometry of the specimen.  
4.8.1. You can use the command (the parameter name is an example):

```python
geom = subprocess.run(["../../../apps/salome_914/salome", "-t", "-w1", "round_specimen_a1_salome_geoms/probka_okragla_a1_salome_geom_15_0_1_5.py"])
```

Note: Instead of the string "user", use your own data, e.g. "john_smith".

4.9. Call the function `gmsh_mesher` providing the parameters: X_length, bar_radius, undercut_radius.  
4.10. Start the FEM analysis using Code_Aster with a parameter being the name of the export script.  
4.10.1. You can use the command (the parameter name is an example):

```python
code_aster = subprocess.run(["as_run", "exports/export_15_0_1_5"])
```

4.11. Launch the ParaView application with a parameter being the name of the script that creates the visualization of the specimen.  
4.11.1. You can use the command (the parameter name is an example):

```python
paraview = subprocess.run(["../../../apps/paraview_5132/bin/pvpython", "round_specimen_a1_salome_pviews/round_specimen_a1_salome_pview_15_0_1_5.py"])
```

Note: Instead of the string "user", use your own data, e.g. "john_smith".

4.12. Set new counter values and return to the beginning of the loop.

### ### ### ### ###
5. Program termination
### ### ### ### ###

5.1. Program termination after the counters reach their max values.  
5.2. Display of the program execution time.  
5.3. The corresponding calculation results can be found in the following directories:  
5.3.1. round_specimen_a1_salome_breps – graphical files of the specimens.  
5.3.2. round_specimen_a1_salome_comms – comm files for Code_Aster.  
5.3.3. round_specimen_a1_salome_geoms – geometry files for Salome Platform.  
5.3.4. round_specimen_a1_salome_meds – mesh files for Code_Aster.  
5.3.5. round_specimen_a1_salome_pngs – graphic files containing calculation results – scalar fields of the stress state triaxiality.  
5.3.6. round_specimen_a1_salome_pviews – batch files for ParaView.  
5.3.7. round_specimen_a1_salome_rmeds – result files from Code_Aster.  
5.3.8. round_specimen_a1_salome_txts – text files with results from Code_Aster. They are used for further analyses with ML – see the elasf_fc repository on GitHub.

### ### ### ### ###
Appendix A. fem_mcip calculations
### ### ### ### ###

A.1. If you want to run the prepared calculations, prepare the system for work.  
A.1.1. Install Git according to section 2.9.  
A.1.2. Create a directory, e.g. analyses. Go to this directory.  
A.1.3. Run the command:

```bash
git clone https://github.com/ennamepro/fem_mcip.git
```

A.1.4. Install and configure Miniconda according to section 2.2 and Appendix B. Remember to install the code_aster 17.0.1 package from the conda-forge repository.  
A.1.5. Install and configure Salome Platform according to section 2.4.  
A.1.6. Install and configure Gmsh according to section 2.5.  
A.1.7. Install and configure ParaView according to section 2.7.  
A.2. Activate the conda environment, e.g. py311.

```bash
conda activate py311
```

A.3. Start the Spyder application with the file round_specimen_a1_stress_concentrator.py loaded:

```bash
spyder round_specimen_a1_stress_concentrator.py
```

Note: Remember the paths to applications and files. All requirements are marked in the program round_specimen_a1_stress_concentrator.py.

A.3.1. Call the Run command (F5).  
A.3.1.1. Due to possible errors, in the counters:

```python
undercut_radius_max = 1.5 # max 12.0
bar_radius_max = 15.0 # max 26.5
```

values were adopted that will cause only a single iteration to be performed.

A.3.1.2. If no errors appear, change the counter parameters to:

```python
undercut_radius_max = 12.0
bar_radius_max = 26.5
```

A.3.1.3. Call the Run command (F5), wait for the program to complete – this may take several hours.

A.4. The analysis results are located in the corresponding directories given in section 5.

### ### ### ### ###
Appendix B. Installation and configuration of the Miniconda environment
### ### ### ### ###

B.1. A complete description of access to resources, their installation and configuration can be found here:

https://www.anaconda.com/docs/getting-started/miniconda/install/linux-install#wget

B.2. After downloading the package, e.g. Miniconda3-py312_24.7.1-0-Linux-x86_64.sh, give it the execute attribute, e.g. `chmod a+x Miniconda3-py312_24.7.1-0-Linux-x86_64.sh`.

B.3. Run the file Miniconda3-py312_24.7.1-0-Linux-x86_64.sh and perform all steps suggested by the installer.

B.3. Create the required environment with the Python 3.11 interpreter.

```bash
conda create -n py311 python=3.11
```

Note: The Miniconda environment 26.1.1-1 of 2026-03-04 contains the following Python interpreters: 3.13.12, 3.12.12, 3.11.14, 3.10.19.

B.4. Activate the created environment:

```bash
conda activate py311
```

B.5. Install the required packages:

```bash
conda install conda-forge::code-aster=17.0.1
conda install spyder=6.0.7
pip install gmsh==4.13.1
```
