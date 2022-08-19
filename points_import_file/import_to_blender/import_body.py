
'''
    This code is used to get access to the text file that store the body points location
    After that, this script will load them to blender
    You can specify the location you store the points file in SOURCE_POINTS_FILE
    8/19/2022 Saliteta

'''



import bpy

SOURCE_POINTS_FILE = "D:\\Xiong_Butian\\blender\\hands\\final_body\\0.txt"


def get_position(path):
    point_cloud = []
    with open(path) as file:
        lines = file.readlines()
        for line_number in lines:
            point_cloud.append((float(line_number.split()[1]),float(line_number.split()[2]),float(line_number.split()[3])))
            print(line_number.split()[1])
            print(line_number.split()[2])
            print(line_number.split()[3])
            print("line")
    return point_cloud

def point_cloud(ob_name, coords, edges=[], faces=[]):
    """Create point cloud object based on given coordinates and name.

    Keyword arguments:
    ob_name -- new object name
    coords -- float triplets eg: [(-1.0, 1.0, 0.0), (-1.0, -1.0, 0.0)]
    """

    # Create new mesh and a new object
    me = bpy.data.meshes.new(ob_name + "Mesh")
    ob = bpy.data.objects.new(ob_name, me)

    # Make a mesh from a list of vertices/edges/faces
    me.from_pydata(coords, edges, faces)

    # Display name and update the mesh
    ob.show_name = True
    me.update()
    return ob

points = get_position(SOURCE_POINTS_FILE)
# Create the object
pc = point_cloud("body", points)

# Link object to the active collection
bpy.context.collection.objects.link(pc)

# Alternatively Link object to scene collection
#bpy.context.scene.collection.objects.link(pc)