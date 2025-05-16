# gammel første utkastet av autoclicker
import mouse, time, keyboard

xValue = 160
yValue = 300

mouse.move(xValue, yValue)

avbryt = False
pause = False

while avbryt == False:
    time.sleep(0.05) # pause sånn at den ikke klikker for fort

    if pause == False:
        mouse.click()

    if keyboard.is_pressed("p"):
        pause = True

    if keyboard.is_pressed("s"):
        pause = False

    if keyboard.is_pressed("q"):
        avbryt = True
    
