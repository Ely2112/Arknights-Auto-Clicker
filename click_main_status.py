import pyautogui
import numpy as np

def click_main_status():
    myScreenshot = np.array(pyautogui.screenshot())

    pyautogui.moveTo(2110/2560*myScreenshot.shape[1], 1250/1440*myScreenshot.shape[0])
    pyautogui.click()

