import cv2
import numpy as np
from Modules import Empty_Fun as EF


def Editor_Parameters(Editor_Name, Hue_min, Sat_min, Val_min, Hue_max, Sat_max, Val_max):

    cv2.namedWindow(Editor_Name)
    cv2.resizeWindow(Editor_Name, 600, 300)
    cv2.createTrackbar("Hue_min", Editor_Name, Hue_min, 179, EF.Empty)
    cv2.createTrackbar("Hue_max", Editor_Name, Hue_max, 179, EF.Empty)
    cv2.createTrackbar("Sat_min", Editor_Name, Sat_min, 255, EF.Empty)
    cv2.createTrackbar("Sat_max", Editor_Name, Sat_max, 255, EF.Empty)
    cv2.createTrackbar("Val_min", Editor_Name, Val_min, 255, EF.Empty)
    cv2.createTrackbar("Val_max", Editor_Name, Val_max, 255, EF.Empty)

def GetFilters(Editor_Name, image):

    ImgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    H_min = cv2.getTrackbarPos("Hue_min", Editor_Name)
    H_max = cv2.getTrackbarPos("Hue_max", Editor_Name)
    S_min = cv2.getTrackbarPos("Sat_min", Editor_Name)
    S_max = cv2.getTrackbarPos("Sat_max", Editor_Name)
    V_min = cv2.getTrackbarPos("Val_min", Editor_Name)
    V_max = cv2.getTrackbarPos("Val_max", Editor_Name)

    Lower = np.array([H_min, S_min, V_min])
    Upper = np.array([H_max, S_max, V_max])

    Mask = cv2.inRange(ImgHSV, Lower, Upper)
    Output = cv2.bitwise_and(image, image, mask=Mask)

    return image, Mask, Output
    #cv2.imshow("Color Picker1", image)
    #cv2.imshow("Color Picker2", Mask)
    #cv2.imshow("Color Picker3", Output)

