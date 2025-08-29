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
            x1 = int(handLms.landmark[4].x * w)
            y1 = int(handLms.landmark[4].y * h)
            x2 = int(handLms.landmark[8].x * w)
            y2 = int(handLms.landmark[8].y * h)
            x3 = int(handLms.landmark[2].x * w)
            y3 = int(handLms.landmark[2].y * h)
            x4 = int(handLms.landmark[3].x * w)
            y4 = int(handLms.landmark[3].y * h)

            # Draw points
            cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (0, 255, 0), cv2.FILLED)

            # Draw line between them
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 3)

            # Calculate distance
            distance = math.hypot(x2 - x1, y2 - y1)

            
            

             # Draw points  v2 so i can mesure distonce
            cv2.circle(img, (x3, y3), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x4, y4), 10, (0, 255, 0), cv2.FILLED)

            # Draw line between them
            cv2.line(img, (x3, y3), (x4, y4), (255, 255, 0), 3)

            # Calculate distance
            distance1 = math.hypot(x4 - x3, y4 - y3)

            
            
            # mesure distance
            dDIV = distance1 / 3
            dis = distance / dDIV * 10 - 10
            # Display distance on screen
            data = str(dis )
            #ser.write((data + "\n").encode())
            cv2.putText(img, f"{int(dis)} mm", (x1, y1 - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


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



