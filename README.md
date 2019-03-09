# partleveler
A script to settle a directory STL files (of arbitrary shape) using Blender physics. If the part starts oriented close to how you'll print it, the script will likely reduce the volume of support structure needed. Before running the script, you will need to position the object above the origin with the relevant surface pointing roughly down and re-export the .stl.

A stationary plane is created which the object is allowed to fall onto. The part will settle into a translation and rotation as if it was dropped onto a table and allowed to balance itself. The script works particularly well for planar things (see below before/after screenshot).

## usage:

### unix:
    <path to blender.exe> -b -P <path to part_leveler.py> -- <path to directory> --unix

### windows:
    <path to blender> -b -P <path to part_leveler.py> -- <path to directory> --windows

### example:
    ./blender -b -P ~/projects/partleveler/part_leveler.py -- ~/stl_dir/ --unix

The dashes are important. Past there, arguments are fed to the python script instead.

![](ugly_but_functional.png)

Let me know if this is useful for you. I originally figured out this process for ridiculously wasteful wax-support style printers that don't care if your part is touching the print bed. 


