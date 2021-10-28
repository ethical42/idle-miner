# idle-miner
Autofarming bot for the Discord bot [Idle Miner](https://top.gg/bot/518759221098053634).

## Installation
1. Download the [`miner.py`](https://raw.githubusercontent.com/ethical42/idle-miner/main/miner.py) file.
2. Install [Python3](https://www.python.org/downloads/) and install the necessary modules:
```
pip3 install pyautogui
pip3 install pyperclip
```
3. Open terminal, go to the directory you saved the `miner.py` file and run the following command in the terminal:
```
python3 miner.py
```
4. Default settings will be 10 seconds on how long it will take until the miner will start executing commands. Therefore make sure to click on the textbox in the channel on Discord so the miner is able to execute the commands.
5. Leave it focused on the input field in the channel on Discord over night or so, and the miner will take care of the rest.
6. Happy autofarming!

## Good to know
Currently `pyautogui.hotkey('command', 'v')` it's for MacOS.
Change `pyautogui.hotkey('command', 'v')` lines to `pyautogui.hotkey('ctrl', 'v')` if you're on Windows machine.

For more info about hotkeys in the PyAutoGui module see [the docs](https://pyautogui.readthedocs.io/en/latest/keyboard.html#the-hotkey-function).
