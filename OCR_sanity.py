import pyautogui
import cv2
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import numpy as np

def return_number(string):
    temp = 0
    for i in string:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            temp *= 10
            temp += int(i)
        elif i == "/":
            break
    return temp

def detect(img_name):
    img = Image.open(img_name).convert("RGB")

    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-large-printed')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-large-printed')
    pixel_values = processor(images=img, return_tensors="pt").pixel_values

    generated_ids = model.generate(pixel_values)
    return processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

def OCR_sanity():
    img = np.array(pyautogui.screenshot())

    cropped_image = img[70:160, 2180:2430]
    grayImage = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    for i in range(blackAndWhiteImage.shape[0]):
        for j in range(blackAndWhiteImage.shape[1]):
            blackAndWhiteImage[i][j] = 0 if blackAndWhiteImage[i][j] == 255 else 255
    cv2.imwrite("sanity/remain_sanity.png", blackAndWhiteImage)
    remain_sanity = return_number(detect("sanity/remain_sanity.png"))


    cropped_image = img[1329:1380, 2189:2450]
    grayImage = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    for i in range(blackAndWhiteImage.shape[0]):
        for j in range(blackAndWhiteImage.shape[1]):
            blackAndWhiteImage[i][j] = 0 if blackAndWhiteImage[i][j] == 255 else 255
    cv2.imwrite("sanity/use_how_many_sanity.png", blackAndWhiteImage)
    use_how_many_sanity = return_number(detect("sanity/use_how_many_sanity.png"))

    print("remain_sanity:       ",remain_sanity)
    print("use_how_many_sanity: ", use_how_many_sanity)

    return int(remain_sanity), int(use_how_many_sanity)
