import pyautogui
from python_imagesearch.imagesearch import *

pyautogui.write('echo \'Hello world!\'\n', interval=0.25)  # prints out "Hello world!" wherever your cursor was with a quarter second delay after each character



# # Controlling the mouse is as easy :
pyautogui.moveTo(x,y,duration=num_seconds)
pyautogui.click(button=button)
# # OR 
# # pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

pos = imagesearch("/images/cloud.JPG")
# pos = imagesearcharea("/images/one.JPG", 0, 0, 800, 600)  #for specific part of pic 1 
if pos[0] != -1:
    print("position : ", pos[0], pos[1])
else:
    print("image not found")


