import numpy as np
from PIL import ImageGrab
import cv2
import time

def process_img(original_image):
    proccessed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    proccessed_img = cv2.Canny(proccessed_img, threshold1=200, threshold2=300)
    return proccessed_img


def screen_record(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode for GTA 5, at the top left position of your main screen.
        # 40 px accounts for title bar. 
        screen =  np.array(ImageGrab.grab(bbox=(0, 50, 800, 600)))
        new_screen = process_img(screen)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()