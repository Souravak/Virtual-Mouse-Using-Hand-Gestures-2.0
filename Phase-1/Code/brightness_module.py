import wmi
import time
c = wmi.WMI(namespace='wmi')
methods = c.WmiMonitorBrightnessMethods()[0]
current_brightness = 50
# for i in range(1,11):
#     brightness = i*10
#     methods.WmiSetBrightness(brightness, 0)
#     time.sleep(0.5)

# global x
# x = 5
# def f():
#     global x
#     x=x+10
# print(x)
# f()
# print(x)

def f():
    # global c
    # global methods
    global current_brightness
    print(methods)

    n = int(input())
    if n%2:
        current_brightness += 10
        current_brightness = min(100, current_brightness)
        methods.WmiSetBrightness(current_brightness, 0)
    else:
        current_brightness -= 10
        current_brightness = max(0, current_brightness)
        methods.WmiSetBrightness(current_brightness, 0)

while(1):
    f()