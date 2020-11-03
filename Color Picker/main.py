import cv2
from Modules import Editor as E

Run = True

FrameWidth = 640
FrameHeight = 320
Width = 3
Height = 4
Brightness = 10
Video_Brightness = 150

Capture = cv2.VideoCapture(0)

Capture.set(Width, FrameWidth)
Capture.set(Height, FrameHeight)
Capture.set(Brightness, Video_Brightness)

E.Editor_Parameters("Editor", 0, 19, 110, 240, 152, 255)

while Run:

    success, Image = Capture.read()
    image, Mask, Output = E.GetFilters("Editor", Image)

    cv2.imshow("Color Picker1", image)
    cv2.imshow("Color Picker2", Mask)
    cv2.imshow("Color Picker3", Output)

    if cv2.waitKey(1) == ord('x'):
        Run = False

