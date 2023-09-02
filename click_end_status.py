import pyautogui
import numpy as np

def click_end_status():
    myScreenshot = np.array(pyautogui.screenshot())

    pyautogui.moveTo(2102/2560*myScreenshot.shape[1], 652/1440*myScreenshot.shape[0])
    pyautogui.click()