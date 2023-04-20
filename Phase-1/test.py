# import pyautogui as pg
# import time
# for i in range(5):
#     # press function key
#     pg.press('brightnessup')

# import wmi
# import time
# c = wmi.WMI(namespace='wmi')
# methods = c.WmiMonitorBrightnessMethods()[0]   
# for i in range(0,100):
#     brightness = i # percentage [0-100] For changing thee screen 
#     methods.WmiSetBrightness(brightness, 0)
#     time.sleep(0.5)


x = 10


def changeX():
    global x
    print("in function", x)


def changeXAgain():
    global x
    x += 100

def changeXAgain():

print(x)
changeX()
print(x)
changeXAgain()
print(x)
