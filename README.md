# sribd_blender
- The purpose of this project is to transform the text to Cue Speech. In other words, is a text to video task
- The demo of the project divided into two parts. The first parts is points location generation, the second part is the points displacement
- There still question to merge hands with face. The future method will be merge a new blender repo to our project

## Google-Mediapipe-Main
- This folder store the essential code to transform a video body movement to corresponding key points location
- The question of the google-mediapipe is that the output will be divided into three part, body, face, and hands
- The output format of those three are not the same

## Points_import_file
- This folder is transform the points generate by google-mediapipe to a blender animation
- The question of the points_import is that it cannot merge three outputs of mediapipe correctly, sometime need to adjust by hands

## BlenderArMocap (cite: https://github.com/cgtinker/BlendArMocap)
- This folder is a plug in develop by another group, the components of this porject will solve our problem
- However, BlenderArMocap is too large for one to completely understand

### demo displacement
![image](https://user-images.githubusercontent.com/88835096/185556550-effee91e-0cc3-4219-95cb-d133c749b9a6.png)
# Transform the video to points
![image](https://user-images.githubusercontent.com/88835096/185556691-7a6265b1-2f60-4584-beed-c31d8d5b751b.png)
# Store the points as txt
![image](https://user-images.githubusercontent.com/88835096/185556920-0608db8d-5fcc-48e8-92bf-9869f112534c.png)
# Display it using blender
![image](https://user-images.githubusercontent.com/88835096/185557074-d71429bc-546c-4d25-9d9d-44249ff3fc97.png)
# Render it with blender

### Thanks to blenderArMocap and pipeMedia
