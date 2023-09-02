import keras
from tqdm import tqdm
import pyautogui
import numpy as np
import cv2
import time

from click_end_status import click_end_status
from click_main_status import click_main_status
from click_team_status import click_team_status

model = keras.models.load_model('status_detection_model.h5')

def screen_status_detection(remain_sanity, use_how_many_sanity):

    game_status = {"0": "battle",
                   "1": "battle_end",
                   "2": "battle_load_color",
                   "3": "battle_load_gray",
                   "4": "black",
                   "5": "end",
                   "6": "end_icon",
                   "7": "main",
                   "8": "sanity",
                   "9": "team"}
    
    total_loop = int(remain_sanity/use_how_many_sanity)

    with open('total_loop.txt', 'w') as f:
        f.write(str(total_loop))

    pbar = tqdm(total=int(remain_sanity/use_how_many_sanity))

    while True:
        if total_loop == 0:
            with open('status.txt', 'w') as f:
                f.write("stop for detection")
            break

        myScreenshot = pyautogui.screenshot()
        myScreenshot = np.array(pyautogui.screenshot())
        myScreenshot = cv2.cvtColor(myScreenshot, cv2.COLOR_BGR2RGB)
        myScreenshot = cv2.resize(myScreenshot, (384, 224))

        y_pred_ = model(np.array([myScreenshot]), training=False)

        text = game_status[str(np.argmax(y_pred_))]

        with open('status.txt', 'w') as f:
            f.write(text)
 
        if  text == "main":
            click_main_status()
            
        elif text == "team":
            click_team_status()
            pbar.update(1)
            with open('total_loop.txt', 'w') as f:
                total_loop -= 1
                f.write(str(total_loop))
            time.sleep(1)

        elif text == "end":
            click_end_status()

        elif text =="sanity":
            break