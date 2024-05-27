import pyautogui
import time
import easyocr
from PIL import ImageGrab
import re

def split_at_capitals(s):
    return re.findall(r'[A-Z][a-z]*', s)

def loading_bar(time_sec):
    for i in  range(time_sec):
        print(f"[{"#"*i}{"_"*(time_sec-i)}] {(time_sec-i)}", end='\r')
        time.sleep(1)
    print(f"[{"#"*time_sec}] {(time_sec-i)}")

# Function to read text from an image using EasyOCR
def read_text_from_image(image):
    # Convert the image to a format suitable for EasyOCR
    image = image.convert('RGB')
    # Save the image to a file-like object in memory
    import io
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()
    
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en'])  # specify the languages you want to use
    # Perform OCR on the image
    results = reader.readtext(image_bytes, detail=0)
    return results

def cords():
    current_mouse_position = pyautogui.position()
    print("Current mouse position:", current_mouse_position)

def capture_screenshot(bbox=None):
    # Capture the screen
    screenshot = ImageGrab.grab(bbox=bbox)
    screenshot.save("fish_name.png")
    return screenshot

def guanenteed_name(y:int):
    pyautogui.moveTo(1213, y, duration=1)
    img = capture_screenshot((1235, 117, 1418, 487))
    fish_name = read_text_from_image(img)
    if len(fish_name) != 0:
            print(fish_name)
            return fish_name[0]
    else:
        return guanenteed_name(y-25)

##Testing the name getter
#cunt = guanenteed_name(405)
#print(cunt)

#time.sleep(5)
#cords()

runCount = 0
while True:
    loading_bar(10)
    print(f"Has run for {runCount} loops")

    ###First talk to the fishermen to get his quests
    pyautogui.moveTo(768, 537, duration=1)
    pyautogui.mouseDown(button="right")
    time.sleep(0.1)
    pyautogui.mouseUp(button='right')

    ### Try 3 then 2 lines positions to check the quest fish
    pyautogui.moveTo(746, 253, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(737, 222, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    #### Hover over the fish, should read fish name and store as text
    pyautogui.moveTo(1215, 318, duration=1)
    time.sleep(2)

    fish = guanenteed_name(476)

    #### From this section we have the fishes name adnn can get it
    pyautogui.keyDown('esc') # This closes the quest menu
    time.sleep(1)
    pyautogui.keyUp('esc')

    pyautogui.keyDown('esc') # This opens the inventory
    time.sleep(1)
    pyautogui.keyUp('esc')

    time.sleep(1)

    #### open the power menue and collect the fish
    pyautogui.moveTo(48, 309, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(47, 528, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(193, 418, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    #### From here need to type the name of the fish
    pyautogui.write(fish, interval=0.5)
    time.sleep(10)
    #### Write the cujnts name here

    ### Grab the fish and move it to ur inventory
    pyautogui.moveTo(148, 446, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(204, 252, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(586, 413, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    #### Give him his fucken fish
    ###First talk to the fishermen to get his quests
    pyautogui.moveTo(768, 537, duration=1)
    pyautogui.mouseDown(button="right")
    time.sleep(0.1)
    pyautogui.mouseUp(button='right')

    ### Try 3 then 2 lines positions to check the quest fish
    pyautogui.moveTo(746, 253, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(737, 222, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')


    #### do the time thing
    pyautogui.keyDown('esc') # This closes the quest menu
    time.sleep(1)
    pyautogui.keyUp('esc')

    pyautogui.keyDown('esc') # This opens the inventory
    time.sleep(1)
    pyautogui.keyUp('esc')

    time.sleep(1)

    pyautogui.moveTo(48, 309, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    time.sleep(2)

    pyautogui.moveTo(41, 632, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(110, 607, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(110, 748, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(110, 607, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    pyautogui.moveTo(110, 748, duration=1)
    pyautogui.mouseDown(button="left")
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

    runCount += 1
