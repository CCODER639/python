import cv2
import serial
import mediapipe as mp
import time
import math
import pyautogui
import threading
from tkinter import *
count = 0
puse = 0
timHold = 0
#print(pyautogui.size())
dis = 40
x11 = 250
y11 = 250
start_time = 0
mesurCo = 0
toTIME = 0
total = 0
def run_tkinter():
    def click():
        global timet
        timet = 1
    def up():
        global puse
        if puse == 1:puse = 0 
        else: puse = 0


    window = Tk()
    window.geometry("200x200")
    window.title("gui program")
    window.config(background="white")
    label = Label(window, text="stop button")
    label.pack()
    button = Button(window, text="stop", command=click)
    button.pack()
    button1 = Button(window, text="puse", command=up)
    button1.pack()

    morse_var = StringVar()
    morse_var.set(dis)

    label1 = Label(window, textvariable=morse_var)
    label1.pack()
 


    def update_morse():
        morse_var.set(dis)
        window.after(100, update_morse)  # update every 100ms

    update_morse()
    window.mainloop()

# Start Tkinter in a separate thread
tk_thread = threading.Thread(target=run_tkinter)
tk_thread.daemon = True
tk_thread.start()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
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
while timet != 1:
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
            cam_x = int(handLms.landmark[5].x * w)
            cam_y = int(handLms.landmark[5].y * h)
            x1 = int(handLms.landmark[2].x * w)
            y1 = int(handLms.landmark[2].y * h)
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

    if puse == 0:
        if dis > 60 or dis < 16:
            screen_x = 3200 - int((cam_x / 1280) * 3600) - 200  # X inverted
            screen_y = int((cam_y / 720) * 2400 -200 )         # Y normal


        if dis > 60:
            pyautogui.moveTo(screen_x, screen_y, duration=0.001)
            if count ==1:
                count = 0
                pyautogui.mouseUp()


        elif dis < 30:

            
 
            t = time.time() - toTIME
            total += t
            toTIME = time.time()
            if count == 0:
                if total > 5:
                    pyautogui.mouseDown()
                    count = 1
                    total = 0

                
                else:
                    pyautogui.click(screen_x, screen_y, duration=0.001)
            elif total > 5:
                pyautogui.moveTo(screen_x, screen_y, duration=0.001)
                print("hi")
        else:
            if count ==1:
                count = 0
                pyautogui.mouseUp()
                total = 0


                


 

                
            




    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 3)


    # Show window
    cv2.imshow("Hand Tracking", img)

    # Press 'q' to exit
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



