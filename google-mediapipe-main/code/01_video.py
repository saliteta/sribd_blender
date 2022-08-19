###############################################################################
### Simple demo with video input
### Input : Live video of face / hand / body
### Output: 2D/2.5D/3D display of face, hand, body keypoint/joint
### Usage : python 01_video.py -m face
###         python 01_video.py -m hand
###         python 01_video.py -m body
###         python 01_video.py -m holistic
###############################################################################

import cv2
import sys
import time
import argparse
import os
import numpy as np

from utils_display import DisplayFaceDetect, DisplayFace, DisplayHand, DisplayBody, DisplayHolistic
from utils_mediapipe import MediaPipeFaceDetect, MediaPipeFace, MediaPipeHand, MediaPipeBody, MediaPipeHolistic


# User select mode
np.set_printoptions(threshold=sys.maxsize)
parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mode', default='hand', 
    help='Select mode: face_detect / face / hand / body / holistic')
args = parser.parse_args()
mode = args.mode

# Load mediapipe and display class
if mode=='face_detect':
    pipe = MediaPipeFaceDetect(model_selection=0, max_num_faces=5)
    pipe = MediaPipeFaceDetect(model_selection=0, max_num_faces=5)
    disp = DisplayFaceDetect()
elif mode=='face':
    pipe = MediaPipeFace(static_image_mode=False, max_num_faces=1, refine_landmarks=True)
    disp = DisplayFace(draw3d=True, refine_landmarks=True)
elif mode=='hand':
    pipe = MediaPipeHand(static_image_mode=False, max_num_hands=2)
    disp = DisplayHand(draw3d=True, max_num_hands=2)
elif mode=='body':
    pipe = MediaPipeBody(static_image_mode=False, model_complexity=1)
    disp = DisplayBody(draw3d=True)
elif mode=='holistic':
    pipe = MediaPipeHolistic(static_image_mode=False, model_complexity=1, refine_face_landmarks=True)
    disp = DisplayHolistic(draw3d=True, refine_face_landmarks=True)
else:
    print('Undefined mode only the following modes are available: \nface / hand / body / holistic')
    sys.exit()

dir = '../data/WT-0431.mp4'
dir3 = '../data/HS-0284.mp4'
dir2 = '../data/video.mp4'
# Start video capture
#cap = cv2.VideoCapture(0) # By default webcam is index 0
cap = cv2.VideoCapture(dir) # Read from .mp4 file
# cap.set(cv2.CAP_PROP_POS_FRAMES, 1) # Set starting position of frame

# Log video
fps = 30
ret, img = cap.read()
width, height = int(cap.get(3)), int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
video = cv2.VideoWriter(dir2, fourcc, fps, (width, height))

prev_time = time.time()
i = 0
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    # Preprocess image if necessary
    #img = cv2.flip(img, 1) # Flip image for 3rd person view
    # img = cv2.resize(img, None, fx=0.5, fy=0.5)

    # To improve performance, optionally mark image as not writeable to pass by reference
    img.flags.writeable = False

    # Feedforward to extract keypoint
    param = pipe.forward(img)

    # Compute FPS
    curr_time = time.time()
    fps = 1/(curr_time-prev_time)
    if mode=='body':
        param['fps'] = fps
    elif mode=='face_detect' or mode=='face' or mode=='hand':
        param[0]['fps'] = fps
    elif mode=='holistic':
        for p in param:
            p['fps'] = fps
    prev_time = curr_time

    img.flags.writeable = True
    # if i < 10 :
    #     with open('C:/Users/41885/Downloads/google-mediapipe-main/google-mediapipe-main/results/keypoint'+'/'+ '0000'+str(i)+'.txt', 'w', encoding='utf-8') as f:  # 使用with open()新建对象f
    #         f.write(str(param))  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
    #     cv2.imwrite('C:/Users/41885/Downloads/google-mediapipe-main/google-mediapipe-main/results/image'+'/'+ '0000'+str(i)+'.jpg',img.copy())
    # if i >= 10  and  i<100:
    #     with open('C:/Users/41885/Downloads/google-mediapipe-main/google-mediapipe-main/results/keypoint'+'/'+ '000'+str(i)+'.txt', 'w', encoding='utf-8') as f:  # 使用with open()新建对象f
    #         f.write(str(param))  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
    #     cv2.imwrite(
    #         'C:/Users/41885/Downloads/google-mediapipe-main/google-mediapipe-main/results/image' + '/' + '000' + str(
    #             i) + '.jpg', img.copy())
    # if i >= 100 :
    #     with open('C:/Users/41885/Downloads/google-mediapipe-main/google-mediapipe-main/results/keypoint'+'/'+ '00'+str(i)+'.txt', 'w', encoding='utf-8') as f:  # 使用with open()新建对象f
    #         f.write(str(param))  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅
    #     cv2.imwrite(
    #         'C:/Users/41885/Downloads/google-mediapipe-main/google-mediapipe-main/results/image' + '/' + '00' + str(
    #             i) + '.jpg', img.copy())

    i = i + 1
    print(i)
    # Display 2D keypoint
    #cv2.imshow('img 2D', disp.draw2d(img.copy(), param))

    # Display 2.5D keypoint
    if mode!='face_detect':
        cv2.imshow('img 2.5D', disp.draw2d_(img.copy(), param))
        # Display 3D
        disp.draw3d(param)
        disp.vis.update_geometry(None)
        disp.vis.poll_events()
        disp.vis.update_renderer()
    img_height, img_width, _ = img.shape
    img2 = np.zeros((img_height,img_width,3), np.uint8)
    img2.fill(255)
    # # Write to video
    img = disp.draw2d(img.copy(), param)
    img2 = disp.draw2d(img2.copy(), param)
    cv2.imshow('img 2D', img)
    cv2.imshow('img 2D', img2)
    video.write(img)

    key = cv2.waitKey(1)
    if key==27:
        break

pipe.pipe.close()
# video.release()
cap.release()
