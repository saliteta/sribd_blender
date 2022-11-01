import mediapipe as mp
import cv2

mp_drawing= mp.solutions.drawing_utils
# draw the detcted land mark directly on the screen
mp_holistic = mp.solutions.holistic
# detect the holitic model


# get real time webcam feed

cap = cv2.VideoCapture(0)

# using base cv2 repo to open the selfie video 
with mp_holistic.Holistic(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as holistic:
    while cap.isOpened(): 
        ret, frame = cap.read()
        # frame is the image itself
        results = holistic.process(frame)
        #print(results.face_landmarks)
        mp_drawing.draw_landmarks(frame, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
        mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        # draw the land mark and lineup
        
        cv2.imshow('Holistic landmark detection', frame)

        if (cv2.waitKey(10) & 0xFF == ord('q')):
            break
cap.release()
cv2.destroyAllWindows()

