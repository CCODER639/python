import cv2
import serial
import mediapipe as mp
import time
import math
import threading
from tkinter import *
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B',
    '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K',
    '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q',
    '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W',
    '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8',
    '----.': '9'
}
adust = 16
string = ""
letterPr = ""
cap = cv2.VideoCapture(0)
timet = 0
button = 0
co = 0
a = 1
prev_time = None
mesurCo = 0
start_time = 0
meCo = 0
mCode = ""
spaceCO = 1
decoded_words = ""

def run_tkinter():
    def click():
        global timet
        timet = 1
    def up():
        global adust
        adust += 2
    def down():
        global adust
        adust -= 2

    window = Tk()
    window.geometry("200x200")
    window.title("gui program")
    window.config(background="white")
    label = Label(window, text="stop button")
    label.pack()
    button = Button(window, text="stop", command=click)
    button.pack()
    button1 = Button(window, text="up", command=up)
    button1.pack()
    button2 = Button(window, text="down", command=down)
    button2.pack()

    morse_var = StringVar()
    morse_var.set(mCode)
    morse_var1 = StringVar()
    morse_var1.set(string)
    label1 = Label(window, textvariable=morse_var)
    label1.pack()
    label2 = Label(window, textvariable=morse_var1)
    label2.pack()


    def update_morse():
        morse_var.set(mCode)
        morse_var1.set(string)
        window.after(100, update_morse)  # update every 100ms

    update_morse()
    window.mainloop()

# Start Tkinter in a separate thread
tk_thread = threading.Thread(target=run_tkinter)
tk_thread.daemon = True
tk_thread.start()

def measure_time(mesurCo, start_time):
    if mesurCo == 0:
        start_time = time.time()
        mesurCo = 1
        return mesurCo, start_time, None
    else:
        stop_time = time.time()
        mesurCo = 0
        elapsed = stop_time - start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed - int(elapsed)) * 1000)
        output = f"{seconds:01d}.{milliseconds:02d}"
        #print(output)
        return mesurCo, start_time, output

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()
##ser = serial.Serial('COM9', 115200)  # Change to your ESP32 port
time.sleep(2)  # wait for connection

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mpDraw = mp.solutions.drawing_utils

pTime = 0
#for teating i added a limit
while timet == 0:
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
            
            if dis < adust:
                if co == 1:
                    co = 0 
                    button += 1
                    print(button)
                    mesurCo, start_time, _ = measure_time(mesurCo, start_time)
                    meCo = 1
            else:
                co = 1
                if spaceCO == 1:
                    if dis > 100:
                        print(" ")
                        mCode += " "
                        spaceCO = 0
                        letters = letterPr.split()
                        decoded_letters = [MORSE_CODE_DICT.get(letter, '?') for letter in letters]
                        decoded_words = ("".join(decoded_letters))
                        print(decoded_words)
                        letterPr = ""
                        string += decoded_words

                if meCo == 1: 
                    mesurCo, start_time, output = measure_time(mesurCo, start_time)
                    meCo = 0
                    if float(output) > 1:
                        print(" / ")
                        mCode += " / "
                       

                    
                    elif float(output) > 0.4:
                        print("-")
                        mCode += "-"
                        letterPr += "-"
                    else:
                        print(".")
                        mCode += "."
                        letterPr += "."
                    spaceCO = 1
                


    # FPS calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime) if pTime else 0
    pTime = cTime









    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 3)

    # Show window
    cv2.imshow("Hand Tracking", img)

    # Check if window was closed by clicking X
    if cv2.getWindowProperty("Hand Tracking", cv2.WND_PROP_VISIBLE) < 1:
        break

    # Press 'q' to exit
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    #timet += 1

cap.release()
cv2.destroyAllWindows()

print(mCode)
file = "hand traking/morse code/morse.txt"
with open(file, "a") as f:
    f.write(str(mCode))
