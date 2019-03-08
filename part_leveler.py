import sys
import bpy
import time
import os

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

print(argv) 

#folder_name = argv[0]
folder_name = ' '.join(argv)
counter = 0

for filename in os.listdir(folder_name):
    if filename.endswith(".stl"):
        counter += 1
        print("({} of {}) processing {}...".format(counter, len(os.listdir(folder_name)), filename))
        #delete starting scene
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
        #bpy.ops.import_mesh.stl(filepath=argv[0])
        bpy.ops.import_mesh.stl(filepath = folder_name + "\\" + filename)
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')
        bpy.context.object.location[0] = 0
        bpy.context.object.location[1] = 0
        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.mass = 1000
        #bpy.ops.screen.animation_play()
        bpy.context.scene.frame_current = 249
        bpy.ops.ptcache.bake_all(bake=False)
        #bpy.ops.export_mesh.stl(filepath = argv[0], use_selection = True)
        bpy.ops.export_mesh.stl(filepath = folder_name + "\\" + filename, use_selection = True)
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
print("Finished leveling {} parts.".format(counter))
