import pygame
import pyautogui
import time

# 🎮 Initialize Joy-Con
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    raise Exception("No Joy-Con detected. Connect via Bluetooth.")

joycon = pygame.joystick.Joystick(0)
joycon.init()

# ⚙️ Config
SPEED = 15
DEADZONE = 0.2
REFRESH_DELAY = 0.005

print("BetterJoy Mini active. Move + click with Joy-Con.")

while True:
    pygame.event.pump()

    x = joycon.get_axis(0)
    y = joycon.get_axis(1)

    dx = int(y * SPEED) if abs(y) > DEADZONE else 0
    dy = int(-x * SPEED) if abs(x) > DEADZONE else 0

    if dx or dy:
        pyautogui.moveRel(dx, dy)

    a = joycon.get_button(1)
    b = joycon.get_button(0)
    home = joycon.get_button(3)  # May vary

    if a:
        pyautogui.click()

    if b:
        pyautogui.click(button='right')

    if home:
        pyautogui.hotkey("ctrl", "esc")  # Admin-free Start menu

    time.sleep(REFRESH_DELAY)
