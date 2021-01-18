import controller_modes
import serial
import time
import webbrowser
import keyboard
# import mido

# TODO: Midi support through mido package and backend...
# TODO: Add third potentiometer, or change two pots out for digital encoders...
# TODO: MacOS Shortcuts... I don't think what I have here will work on my work laptop (shortcuts mode)

ser = serial.Serial('COM3', 9600)
time.sleep(2)
mode = controller_modes.shortcut.get()
p = 'v0'
p1 = 0 #p1 prints serial as p* for better compatibility with string.strip()
p2 = 0 # p@
p3 = 0 # p$


def set_mode(int_value):
    if int_value <= 85:
        return controller_modes.web_mode.get()
    elif int_value <= 170:
        return controller_modes.work_web_mode.get()
    else:
        return controller_modes.shortcut.get()

while True:
    d = ser.readline()
    str_rn = d.decode()
    solid = str_rn.rstrip()

    if solid.__contains__('p*'):
        p1 = int(solid.strip('p*:'))
        mode = set_mode(p1)
    elif solid.__contains__('p@'):
        p2 = int(solid.strip('p@:'))
    elif solid.__contains__('p$'):
        p3 = int(solid.strip('p$:'))
    
    if solid != p:
        # print(solid)
        p = solid

        for k,v  in mode.items():
            if k in solid:
                # print("key: " + k)
                # print("value: " + v)
                if mode['mode'] == 'web' or mode['mode'] == 'work_web':
                    webbrowser.open(v)
                if mode['mode'] == 'shortcut':
                    keyboard.press_and_release(v)
