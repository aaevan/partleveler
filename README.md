# partleveler
A script to settle a directory STL files (of arbitrary shape) using Blender physics, probably reducing the volume of support structure needed.

The part will settle to about what you'd expect it to look like if it was placed on a table.

It works particularly well for planar things (see below before/after screenshot).

## usage:

### unix:
    <path to blender.exe> -b -P <path to part_leveler.py> -- <path to directory> --unix

### windows:
    <path to blender> -b -P <path to part_leveler.py> -- <path to directory> --windows

### example:
    ./blender -b -P ~/projects/partleveler/part_leveler.py -- ~/stl_dir/ --unix

The dashes are important, it indicates to blender to ignore past there and let the python script handle that input instead.

![before and after](ugly_but_functional.png)

Let me know if this is useful for you. I originally figured out this process for ridiculously wasteful wax-support style printers that don't even care if your part is touching the print bed. 


