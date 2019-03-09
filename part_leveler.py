import sys
import bpy
import time
import os

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

print(argv) 

folder_name = argv[0]
counter = 0

if '--windows' in argv:
    slash_style = '\\'
elif '--unix' in argv:
    slash_style = '/'
else:
    print("Please choose a path style by appending --windows or --unix.")
    exit()

for filename in os.listdir(folder_name):
    if filename.endswith(".stl"):
        counter += 1
        print("({} of {}) processing {}...".format(counter, len(os.listdir(folder_name)), filename))
        #for good measure, delete everything
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

        #create a plane and assign properties
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.resize(value=(40, 40, 40))
        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.mass = 1000
        bpy.context.object.rigid_body.type = 'PASSIVE'
        bpy.ops.object.select_all(action='DESELECT')

        #import stl and assign properties
        file_path = folder_name + slash_style + filename
        bpy.ops.import_mesh.stl(filepath = file_path)
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')
        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = 0
        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.mass = 1000

        #simulate 249 frames of animation
        bpy.context.scene.frame_current = 249
        bpy.ops.ptcache.bake_all(bake=False)

        #export settled mesh in place
        bpy.ops.export_mesh.stl(filepath = file_path, use_selection = True)

        #delete everything again in preparation for the next stl
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
print("Finished leveling {} parts.".format(counter))
