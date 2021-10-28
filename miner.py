import pyautogui
import pyperclip
import time
from time import strftime
from time import gmtime
import datetime
import random

actionWait = 120 # Change this value if needed
wait_time = 3 # Change this value if needed

counter_birth = 0
sellLoop = 1
loops = 0
total_loops = 0
hour_run = 0
start_time = time.time()

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

current_hour = datetime.datetime.now().strftime("%H")    
hours = int(current_hour)

n = 8
for i in range(n):
    print( " "*(n-i-1) + "*"*(2*i+1) )

print("**-Idle miner-**")
print("*To your service*")
print()

print("[System]: Booting...")
print()
time.sleep(1)
print("[FYI]: Between each action there's a default cooldown for 3 seconds")
print("[FYI]: Change the cooldown in miner.py on line: 10")
print()
time.sleep(1)

x = 10
while x > 0:
    print("[Info]: Executing actions in", x, "seconds")
    
    x -= 1
    time.sleep(1)

print("[Info]: Executing actions...")
time.sleep(1)
print()

while sellLoop == 1:
    if total_loops > 0:
        print("[Info]: Executing actions...")
        print()
        time.sleep(wait_time)
    
    pyperclip.copy(';sell')
    pyautogui.press("enter")

    pyperclip.copy(';sell')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("[Action]: Sold")

    time.sleep(wait_time)

    if hours > hours-1 and hour_run == 0:
        pyperclip.copy(';hourly')
        pyautogui.hotkey('command', 'v')
        pyautogui.press("enter")
        print("[Action]: Hour reward claimed")
        
        hour_run = 0
        time.sleep(wait_time)

    if loops > 2:
        pyperclip.copy(';level')
        pyautogui.hotkey('command', 'v')
        pyautogui.press("enter")
        print("[Action]: Leveled")
        
        loops = 0
        time.sleep(wait_time)

    pet = random.choice(pets)
    string = ';up '+pet+' a'
    
    pyperclip.copy(string)
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("[Action]: Upgrading "+ pet.title() +" pet")
    
    time.sleep(actionWait)
    
    pyperclip.copy(';sell')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("[Action]: Sold")
    
    time.sleep(wait_time)

    pyperclip.copy(';fish')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("[Action]: Fished")

    time.sleep(wait_time)

    pyperclip.copy(';up b a')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("[Action]: Upgraded backpack")
    
    time.sleep(actionWait)

    pyperclip.copy(';sell')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("[Action]: Sold")

    time.sleep(wait_time)

    pyperclip.copy(';up p a')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("[Action]: Upgraded pickaxe")
    
    time.sleep(wait_time)

    pyperclip.copy(';hunt')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("[Action]: Hunted")

    time.sleep(actionWait)

    pyperclip.copy(';sell')
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    print("[Action]: Sold")
    
    print()
    current_time = time.time()
    elapsed_time = current_time - start_time

    print("[Info]: Current time: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    print("[Info]: Time running: " + strftime("%H:%M:%S", gmtime(elapsed_time)))

    if total_loops > 0:
        print("[Info]: Total Loops:", total_loops)
        print("[Info]: Looping again...")
    else:
        print("[Info]: First loop done")
        print("[Info]: Looping again...")
    
    if counter_birth > 50:
        print()
        pyperclip.copy(';rebirth')
        pyautogui.hotkey('command', 'v')
        pyautogui.press("enter")
        print("[Action]: You just started a new life")

        counter_birth = 0

    counter_birth += 1
    hour_run = 1
    loops += 1
    total_loops += 1