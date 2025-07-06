🎮 BetterJoy Project
Tykniter Input Enhancement Tools
Welcome to BetterJoy and BetterJoy_Mini — a pair of Python scripts that turn your Nintendo Joy-Con into a surprisingly effective cursor, clicker, and chaos trigger device for Windows desktops. Whether you're running a full LED control panel or just want raw input control, you're covered.

🧩 BetterJoy.py
A GUI-based controller dashboard with glowing LED ring, click simulation, and button remaps.

Features
🖱 Cursor movement via joystick

✅ A = Left Click, B = Right Click

🪟 HOME = Windows Key (simulated safely via ctrl + esc)

🎛 LED visualizer modes: Solid, Breathing, Heartbeat, Off

🧠 Live status and ΔX/ΔY tracking

Requirements
Python 3.x

pygame, pyautogui, tkinter (built-in), time

Run It
bash
python BetterJoy.py
⚡ BetterJoy_Mini.py
Minimal console-only script for movement and button handling. No GUI. No distractions.

Features
🎮 Joystick-driven cursor movement

💻 Basic button mapping:

A = Left Click

B = Right Click

HOME = Start Menu (via ctrl + esc)

💤 Lightweight, fast, and perfect for background use

Requirements
Python 3.x

pygame, pyautogui

Run It
bash
python BetterJoy_Mini.py
🔧 Notes
Connect Joy-Con via Bluetooth before launching either script

HOME button index may vary by Joy-Con model (default = get_button(3))

Use the GUI version for LED flair and debugging, or MINI for stealth input ops

🌀 License & Credit
Created by Rowan Tykniter Certified. Chaos Verified. Use freely. Modify rebelliously.
