import pyautogui
import time

def loading_bar(time_sec):
    for i in  range(time_sec):
        print(f"[{"#"*i}{"_"*(time_sec-i)}] {(time_sec-i)}", end='\r')
        time.sleep(1)
    print(f"[{"#"*time_sec}] {(time_sec-i)}")

def movement_to_angler():
    ##Make sure normalised
    pyautogui.keyDown('d')
    time.sleep(1)
    pyautogui.keyUp('d')

    ##Now we need to walk to the top of the stairs
    pyautogui.keyDown('a')
    loading_bar(5)
    pyautogui.keyUp('a')

    ##Now we drop down 1 stiar
    pyautogui.keyDown('s')
    time.sleep(1)
    pyautogui.keyUp('s')

    ##Now we need to walk to the anglers door
    pyautogui.keyDown('d')
    time.sleep(1)
    pyautogui.keyUp('d')

def interact(x_positions, y_position, button):
    for i in x_positions:
        pyautogui.moveTo(i, y_position, duration=1)
        pyautogui.mouseDown(button=f"{button}")
        time.sleep(1)
        if button == 'left':
            pyautogui.mouseUp(button='left')
        elif button == 'right':
            pyautogui.mouseUp(button='right')

def clean_screen():
    pyautogui.keyDown('esc')
    time.sleep(1)
    pyautogui.keyUp('esc')

def cords():
    current_mouse_position = pyautogui.position()
    print("Current mouse position:", current_mouse_position)

def movement_to_chest():
    ##Walk back to wall
    pyautogui.keyDown('a')
    time.sleep(1)
    pyautogui.keyUp('a')

    ##jump up the stair
    pyautogui.keyDown('space')
    time.sleep(3)
    pyautogui.keyUp('space')

    ##walk back to chest into normal position
    pyautogui.keyDown('d')
    time.sleep(8)
    pyautogui.keyUp('d') 

def move_single(direction):
    pyautogui.keyDown(f"{direction}")
    time.sleep(8)
    pyautogui.keyUp(f"{direction}")


running_count = 0

##Give yoursefl sometime to get into position
loading_bar(5)

##Move to angler
while True:
    move_single('d')

    ##Open first chest and loot all
    interact([954], 547, 'right')
    interact([572], 326, 'left')
    interact([997, 1016], 542, 'right')
    interact([738], 259, 'left')
    interact([738], 221, 'left')
    interact([954], 547, 'right')
    interact([601], 353, 'left')

    ##Open second chest and loot all
    interact([920], 546, 'right')
    interact([572], 326, 'left')
    interact([997, 1016], 542, 'right')
    interact([738], 259, 'left')
    interact([738], 221, 'left')
    interact([920], 546, 'right')
    interact([601], 353, 'left')

    ##Open third chest and loot all
    interact([939], 509, 'right')
    interact([572], 326, 'left')
    interact([997, 1016], 542, 'right')
    interact([738], 259, 'left')
    interact([738], 221, 'left')
    interact([939], 509, 'right')
    interact([601], 353, 'left')

    move_single('a')

    clean_screen()

    interact([968], 550, 'right')

    running_count += 1

    print(f"Loop has run {running_count} times")

    loading_bar(400)