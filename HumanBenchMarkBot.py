import pyautogui
from PIL import Image
import cv2
from pynput.keyboard import Listener
import keyboard
import time
import numpy as np

running = True



startPosition = [760,235]

endPosition = [427, 400]

whiteExists = False




while running:


    if keyboard.is_pressed('esc'):
       running = False
       break

    im = pyautogui.screenshot("image" + '.png', region=(760,235, 427, 400))
    img = Image.open("image" + str(imageName)+ '.png')
    px = img.load() 

  

    cordinate = [0, 0]
    point = []
     
       

    while cordinate[1] < endPosition[1]:      
        
        if px[cordinate[0], cordinate[1]][0] >= 230 and px[cordinate[0], cordinate[1]][1] >= 230 and px[cordinate[0], cordinate[1]][2] >= 230:

            whiteExists = True
            point.append([cordinate[0], cordinate[1]])
       
        if cordinate[0] < 420:
            cordinate[0] += 10
            
         
            
        else:
            cordinate[0] = 0
            cordinate[1] += 10

    
    if whiteExists:
        time.sleep(1)
        i = 0

        while len(point) > i:

            pyautogui.moveTo(point[i][0] + 760, point[i][1] + 235, _pause=False)

            pyautogui.click(_pause=False)
            
            i += 1
         
        
        time.sleep(2)

  