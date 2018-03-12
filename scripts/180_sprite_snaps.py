import bpy
from math import radians

step_count = 13
selected = bpy.context.selected_objects[0]

target_dir = 'C:\\Users\\skate\\Desktop\\'

for step in range(0, step_count):
    for obj in bpy.data.objects:
        if obj.type != "CAMERA" and obj.type != "LAMP":
            obj.rotation_euler[2] = radians(step * (180.0 / step_count))

    bpy.data.scenes["Scene"].cycles.film_transparent = True
    bpy.data.scenes["Scene"].render.filepath = '%s%s%d.jpg' % (target_dir, selected.name, step)
    bpy.ops.render.render( write_still=True )
