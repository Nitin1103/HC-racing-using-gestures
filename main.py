import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.5, maxHands=2)
cap = cv2.VideoCapture(0) # 0 for the first webcam, 1 for the second webcam, etc.

cap.set(3, 640) # Set the width of the frame
cap.set(4, 480) # Set the height of the frame

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) # Flip the frame horizontally
    hand, img = detector.findHands(img)
    if hand and hand[0]['type'] == 'Left':
        fingers = detector.fingersUp(hand[0])
        totalFingers = fingers.count(1)
        cv2.putText(img, f"Fingers: {totalFingers}", (50,50), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255), 2)
        if totalFingers == 5:
            pyautogui.keyDown('right')
            pyautogui.keyUp('left')
        if totalFingers == 0:
            pyautogui.keyDown('left')
            pyautogui.keyUp('right')

    cv2.imshow("Camera feed", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break