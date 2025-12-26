import mediapipe as mp
import cv2
import pydirectinput

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose

pydirectinput.FAILSAFE = False
pydirectinput.PAUSE = 0.05

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    exit()

with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as holistic:

    while True:
        ret, image = cap.read()
        if not ret:
            break

        image = cv2.flip(image, 1)
        height, width, _ = image.shape
        y_mid = height // 2

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = holistic.process(rgb)

        status = "IDLE"

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

            right_wrist_y = int(
                results.pose_landmarks.landmark[
                    mp_pose.PoseLandmark.RIGHT_WRIST
                ].y * height
            )

            left_wrist_y = int(
                results.pose_landmarks.landmark[
                    mp_pose.PoseLandmark.LEFT_WRIST
                ].y * height
            )

            if left_wrist_y < y_mid:
                pydirectinput.keyDown('right')
                pydirectinput.keyUp('left')
                status = "ACCELERATE"

            elif right_wrist_y < y_mid:
                pydirectinput.keyDown('left')
                pydirectinput.keyUp('right')
                status = "BRAKE"


        cv2.putText(
            image,
            status,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Hill Climb", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows() 
