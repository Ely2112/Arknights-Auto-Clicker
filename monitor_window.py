import pyautogui
import numpy as np
import cv2

def monitor_window(remain_sanity, use_how_many_sanity):

    previous = "initial"
    previous_2 = int(remain_sanity/int(use_how_many_sanity))

    while True:
        myScreenshot = pyautogui.screenshot()
        myScreenshot = np.array(myScreenshot)
        myScreenshot = cv2.cvtColor(myScreenshot, cv2.COLOR_BGR2RGB)

        myScreenshot = cv2.resize(myScreenshot,(int(myScreenshot.shape[1]/2), int(myScreenshot.shape[0]/2)))

        with open('status.txt') as f:
            TEXT = f.readlines()

        with open('total_loop.txt') as f:
            TEXT_total_loop = f.readlines()
        

        # start_point = (40, 30)
        # end_point = (600, 130)
        # color = (30, 30, 30)
        # thickness = -1
        # myScreenshot = cv2.rectangle(myScreenshot, start_point, end_point, color, thickness)

        overlay_myScreenshot = myScreenshot.copy()

        cv2.rectangle(overlay_myScreenshot, (40, 30), (700, 130), (30, 30, 30), -1)

        alpha = 0.4 # Transparency factor.

        # Following line overlays transparent rectangle
        # over the image
        myScreenshot = cv2.addWeighted(overlay_myScreenshot, alpha, myScreenshot, 1 - alpha, 0)


        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # org
        org = (400, 60) # right, down
        org_2 = (400, 120)
        org_3 = (50, 60)
        org_4 = (50, 120)
        
        # fontScale
        fontScale = 1
        
        # Blue color in BGR
        color = (230, 230, 230)
        
        # Line thickness of 2 px
        thickness = 2

        try:
            previous = current_status = TEXT[0]
        except IndexError:
            current_status = previous

        try:
            previous_2 = total_loop = TEXT_total_loop[0]
        except IndexError:
            total_loop = previous_2

        myScreenshot = cv2.putText(myScreenshot, current_status, org, font, fontScale, color, thickness, cv2.LINE_AA)
        myScreenshot = cv2.putText(myScreenshot, total_loop, org_2, font, fontScale, color, thickness, cv2.LINE_AA)
        myScreenshot = cv2.putText(myScreenshot, "Current Status:", org_3, font, fontScale, color, thickness, cv2.LINE_AA)
        myScreenshot = cv2.putText(myScreenshot, "Remain Loop Round:", org_4, font, fontScale, color, thickness, cv2.LINE_AA)

        cv2.namedWindow('Auto Clicker Monitor')
        cv2.moveWindow('Auto Clicker Monitor', 4400, 200)

        if current_status != "initial":
            cv2.imshow('Auto Clicker Monitor', myScreenshot)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break