# partleveler
A script to level a directory STL files (of arbitrary irregularity) using Blender physics, minimizing the volume of support structure needed.

usage:
blender -b -P \<path to part_leveler.py\> -- \<path to folder to iterate over\>

The dashes are important, it indicates to blender to ignore past there and let the python script handle that input instead.

Comment out lines labeled unix and windows to toggle between directory styles.

![](ugly_but_functional.png)
