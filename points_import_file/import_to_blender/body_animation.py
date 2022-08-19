'''
    Here is the script that can transform the entire folder of points to animation
'''



import bpy
import bmesh
import numpy as np

FRAME_NUM = 303
SOURCE_POINTS_FOLDER = "D:\\Xiong_Butian\\blender\\hands\\final_body\\"

def get_position(path):
    point_cloud = []
    with open(path) as file:
        lines = file.readlines()
        i = 0
        for line_number in lines:
            i += 1
            try:
                point_cloud.append((float(line_number.split()[1]),float(line_number.split()[2]),float(line_number.split()[3])))
            except:
                print(i)
                print(line_number.split()[1])
                print(line_number.split()[2])
                print(line_number.split()[3])
    return point_cloud

## ------- part 1 --- do this once.
n_frames = FRAME_NUM
bpy.context.scene.frame_end = n_frames

obj = bpy.context.active_object # change it to be the lips/ cloud point
me = obj.data


data = []

for i in range(n_frames):
    point_cloud = get_position("D:\\Xiong_Butian\\blender\\hands\\final_body\\"+str(i)+'.txt')
    ico = np.asarray(point_cloud)
    data.append(ico.copy())
    

for i_frame in range(n_frames):
    block = obj.shape_key_add(name=str(i_frame), from_mix=False)  # returns a key_blocks member
    block.value = 1.0
    block.mute = True
    for (vert, co) in zip(block.data, data[i_frame]):
        vert.co = co

    # keyframe off on frame zero
    block.mute = True
    block.keyframe_insert(data_path='mute', frame=0, index=-1)

    block.mute = False
    block.keyframe_insert(data_path='mute', frame=i_frame + 1, index=-1)

    block.mute = True
    block.keyframe_insert(data_path='mute', frame=i_frame + 2, index=-1)  

print("finished")