from psychopy import visual
import cv2

win = visual.Window([800,600])
webCam = cv2.VideoCapture(0)

# create your stimulus (top of script)
                           flipVert=True)  # webcam reads bottom to top
    