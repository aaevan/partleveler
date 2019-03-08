# partleveler
A script to level a directory STL files (of arbitrary irregularity) using Blender physics, minimizing the volume of support structure needed.

usage:
blender -b -P \<path to part_leveler.py\> -- \<path to folder to iterate over\>

The dashes are important, it indicates to blender to ignore past there and let the python script handle that input instead.
