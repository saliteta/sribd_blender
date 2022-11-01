# sribd_blender
- The purpose of this project is to transform the text to Cue Speech. In other words, is a text to video task
- The demo of the project divided into two parts. The first parts is points location generation, the second part is the points displacement
- There still question to merge hands with face. The future method will be merge a new blender repo to our project

## Google-Mediapipe-Main (cite: MediaPipe: A Framework for Building Perception Pipelines  https://arxiv.org/pdf/1906.08172.pdf)
- This folder store the essential code to transform a video body movement to corresponding key points location
- The question of the google-mediapipe is that the output will be divided into three part, body, face, and hands
- The output format of those three are not the same

## Points_import_file
- This folder is transform the points generate by google-mediapipe to a blender animation
- The question of the points_import is that it cannot merge three outputs of mediapipe correctly, sometime need to adjust by hands

## BlenderArMocap (cite: https://github.com/cgtinker/BlendArMocap)
- This folder is a plug in develop by another group, the components of this porject will solve our problem
- However, BlenderArMocap is too large for one to completely understand

# demo displacement


Detection             |  Output 3D location
:-------------------------:|:-------------------------:
<img src = "https://user-images.githubusercontent.com/88835096/185556550-effee91e-0cc3-4219-95cb-d133c749b9a6.png">  |   <img src = "https://user-images.githubusercontent.com/88835096/185556691-7a6265b1-2f60-4584-beed-c31d8d5b751b.png">


Import to Blender | Render Motion with Predefined Model
:-------------------------:|:-------------------------:
 <img src = "https://user-images.githubusercontent.com/88835096/185556920-0608db8d-5fcc-48e8-92bf-9869f112534c.png"> |<img src = "https://user-images.githubusercontent.com/88835096/185557074-d71429bc-546c-4d25-9d9d-44249ff3fc97.png">


### Thanks to blenderArMocap and pipeMedia

# csc3185
- After do some improvement to the SRIBD project, use it as a project in CSC3185
## Improvement1： Transform the video to csv.
<p align = "center">
<img src = "https://user-images.githubusercontent.com/88835096/199153540-8d9b489e-08e7-4e7d-902b-9409d9266527.png">
</p>


## Improvement2: Whisper (cite this paper: Robust Speech Recognition via Large-Scale Weak Supervision https://cdn.openai.com/papers/whisper.pdf)
- transcrip people's voice to text
- test code in whisper.ipynb
<p align= "center">
  <img src = "image/mp3.jpg" />
 </p>
 <p align= "center">
  <img src = "https://user-images.githubusercontent.com/88835096/199153858-799ffe9b-d7b1-4abf-b077-4bd0f4b0f571.png" />
 </p>
 
## Improvement3: Sentiment Analysis (cite this paper: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding https://arxiv.org/abs/1810.04805)
- Do the compueter vision analysis using the feature extracted from the video sequence
- Do the natural language processing using the BERT model analize the text extract from the video sequence


 Expression Analysis through Video            |  Expression Analysis through Audio
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/88835096/199207384-e2a06c96-2857-4fdf-9cd5-0094928832c5.png)　|   ![image](https://user-images.githubusercontent.com/88835096/199207896-6a6963e0-3a42-4bb7-8686-f0baa06e4dad.png)



## Future work:
- improving the connection of hands and faces by reading the file of blenderArMocap
- adding the generation model to the google-mediapipe
