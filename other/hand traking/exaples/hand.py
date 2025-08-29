import cv2
import serial
import mediapipe as mp
import time
import math
cap = cv2.VideoCapture(0)
timet = 0
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()
##ser = serial.Serial('COM9', 115200)  # Change to your ESP32 port
time.sleep(2)  # wait for connection

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mpDraw = mp.solutions.drawing_utils

pTime = 0
#for teating i added a limit
while timet != 1000:
    success, img = cap.read()
    if not success:
        print("Failed to capture image from camera.")
        break

    # Convert to RGB for MediaPipe
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c= img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)



    # FPS calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime) if pTime else 0
    pTime = cTime









    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 3)

    # Show window
    cv2.imshow("Hand Tracking", img)

    # Press 'q' to exit
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    timet += 1

cap.release()
cv2.destroyAllWindows()



