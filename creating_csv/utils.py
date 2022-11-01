import os
import numpy as np
import pandas as pd


# x, y, z, and visual

def save_csv(class_name, id, result, face = True, pose = False):
    '''
        Give the correspoinding classname and the face_list structure.
        This model will automatically store the csv to corresponding folder

        May be we need to also generate a unique id for each csv file

        result should be the result generate by pipeline
    '''

    if face:
        pose = result.face_landmarks.landmark
        pose_row = np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose])
            
        df = pd.DataFrame(pose_row, columns= ['x', 'y', 'z', 'v'])
        df.to_csv(f"./train/{class_name}/face/{id}.csv")
    if pose:
        pose = result.pose_landmarks.landmark
        pose_row = np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose])
        df = pd.DataFrame(pose_row, columns= ['x', 'y', 'z', 'v'])
        df.to_csv(f"./train/{class_name}/pose/{id}.csv")



def create_dir(class_list, sub_folder = ['face', 'pose', 'left_hand', 'right_hand'], train = True, val = True):
    try:
        os.rmdir('train')
        os.rmdir('val')
    except:
        print('train or val folder is not create, now create for you')

    if train:
        os.mkdir('train')
        for each_class in class_list:
            os.mkdir(f'./train/{each_class}')
            for land_mark_folder in sub_folder:
                os.mkdir(f'./train/{each_class}/{land_mark_folder}')
    if val:
        os.mkdir('val')
        for each_class in class_list:
            os.mkdir(f'./val/{each_class}')
            for land_mark_folder in sub_folder:
                os.mkdir(f'./val/{each_class}/{land_mark_folder}')

if __name__ == '__main__':
    create_dir(['happy', 'sad', 'anxious', 'angry'])