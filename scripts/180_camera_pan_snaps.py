import bpy
from math import radians, fabs

step_count = 5
pan_angle = 60
pan_span = 4.5

pan_start = 1 / pan_span
pan_end = -pan_start

camera = [obj for obj in bpy.data.objects if obj.type == "CAMERA"]
assert camera
camera = camera[0]

camera.location[1] = pan_start
camera.rotation_euler[2] -= radians(pan_angle / 2)

for step in range(0, step_count):
    camera.location[1] = step * (1 / (fabs(pan_start) + fabs(pan_end)))
    camera.rotation_euler[2] = radians(step * (pan_angle / step_count))

    bpy.data.scenes["Scene"].cycles.film_transparent = True
    bpy.data.scenes["Scene"].render.filepath = 'C:\\Users\\skate\\Desktop\\camera_pan_%d.jpg' % step
    bpy.ops.render.render( write_still=True )