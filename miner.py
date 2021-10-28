import pyautogui
import pyperclip
import time
import datetime
import random

actionWait = 120
counter_birth = 0
sellLoop = 1
loops = 0
total_loops = 0
hour_run = 0

pets = [
    'bat',
    'cow',
    'pig',
    'sheep',
    'squid',
    'chicken',
    'creeper',
    'ocelot',
    'pufferfish',
    'wolf',
    'dolphin',
    'enderman',
    'guardian',
    'parrot',
    'turtle',
    'elder-guardian',
    'iron-golem',
    'snow-golem',
    'villager',
    'wither-skeleton',
    'zombie-horse',
    'skeleton-horse',
    'spider-jockey',
    'ender-dragon',
    'wither',
    'giant',
]

# Get date time and convert to a string
time_now = datetime.datetime.now().strftime("%H")    
hours = int(time_now)

while sellLoop == 1:
    
    print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Executing actions...")
    time.sleep(10)
    
    pyperclip.copy(';sell')
    pyautogui.press("enter")

    if hours > hours-1 and hour_run == 0:
        pyperclip.copy(';hourly')
        pyautogui.hotkey('command', 'v')
        pyautogui.press("enter")
        print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Hour reward claimed...")
        
        hour_run = 0
        time.sleep(3)

    if loops > 2:
        pyperclip.copy(';level')
        pyautogui.hotkey('command', 'v')
        pyautogui.press("enter")
        print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Leveled...")
        
        loops = 0
        time.sleep(3)

    pet = random.choice(pets)
    string = ';up '+pet+' a'
    
    pyperclip.copy(string)
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Upgrading "+ pet.title() +" pet...")
    
    time.sleep(actionWait)
    
    pyperclip.copy(';sell')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Sold...")
    
    time.sleep(3)

    pyperclip.copy(';fish')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Fished...")

    time.sleep(3)

    pyperclip.copy(';up b a')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Upgraded backpack...")
    
    time.sleep(actionWait)

    pyperclip.copy(';sell')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Sold...")

    time.sleep(3)

    pyperclip.copy(';up p a')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Upgraded pickaxe...")
    
    time.sleep(3)

    pyperclip.copy(';hunt')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Hunted...")

    time.sleep(actionWait)

    pyperclip.copy(';sell')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Sold...")
    
    if total_loops > 0:
        print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: All done! Total loops:",total_loops)
        print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: Looping again...")
    else:
        print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: First loop done. Looping again...")
    
    if counter_birth > 50:
        pyperclip.copy(';rebirth')
        pyautogui.hotkey('command', 'v')
        pyautogui.press("enter")
        print("["+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"]: You just started a new life!")

        counter_birth = 0

    counter_birth += 1
    hour_run = 1
    loops += 1
    total_loops += 1