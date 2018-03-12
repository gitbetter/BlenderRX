## 180_camera_pan_snaps.py
Moves the camera in a `pan_angle` degree arc, taking as many as `step_count` render 
snaps and saving them to `target_dir`. This is useful if you are trying to do discrete
sprite animations using 3D models.

## 180_sprite_snaps.py
Rotates all objects in the scene (except the camera and lights) by 180 degrees from
their default Y rotations. Mainly used to create spritesheets and sprite animations
from 3D renders, but the uses are unbounded.
