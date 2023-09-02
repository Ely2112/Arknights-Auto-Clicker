import os
from multiprocessing import Process

from monitor_window import monitor_window
from OCR_sanity import OCR_sanity
from screen_status_detection import screen_status_detection

if __name__ == '__main__':

    with open('status.txt', 'w') as f:
        f.write("initial")

    os.environ["CUDA_VISIBLE_DEVICES"]="0"
    
    
    remain_sanity, use_how_many_sanity = OCR_sanity()

    total_loop = int(remain_sanity/int(use_how_many_sanity))

    with open('total_loop.txt', 'w') as f:
        f.write(str(total_loop))
    

    p1 = Process(target=screen_status_detection, args=(remain_sanity, use_how_many_sanity))
    p1.start()
    p2 = Process(target=monitor_window, args=(remain_sanity, use_how_many_sanity))
    p2.start()