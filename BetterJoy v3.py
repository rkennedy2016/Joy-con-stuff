import tkinter as tk
import math
import pygame
import pyautogui
import threading
import time

# 🎮 Initialize Joy-Con
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    messagebox.showerror("No Joy-Con detected", "No Joy-Con connected. Connect via Bluetooth.")

joycon = pygame.joystick.Joystick(0)
joycon.init()

# ⚙️ Config
SPEED = 15
DEADZONE = 0.2
REFRESH_DELAY = 0.005

class BetterJoy:
    def __init__(self, root):
        self.root = root
        self.root.title("BetterJoy - Tykniter Edition")
        self.root.geometry("400x420")
        self.root.configure(bg="#0a0a0a")

        tk.Label(root, text="🎮 BetterJoy Control Panel", fg="cyan",
                 bg="#0a0a0a", font=("Consolas", 14, "bold")).pack(pady=10)

        self.status = tk.Label(root, text="Status: Waiting for input", fg="white",
                               bg="#0a0a0a", font=("Consolas", 10))
        self.status.pack()
        self.coords = tk.Label(root, text="ΔX: 0 | ΔY: 0", fg="white",
                               bg="#0a0a0a", font=("Consolas", 10))
        self.coords.pack()

        self.canvas = tk.Canvas(root, width=100, height=100,
                                bg="#0a0a0a", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.led_ring = self.canvas.create_oval(10, 10, 90, 90,
                                                outline="#001122", width=6)

        self.mode = tk.StringVar(value="Heartbeat")
        for m in ["Solid", "Breathing", "Heartbeat", "Off"]:
            tk.Radiobutton(root, text=m, variable=self.mode, value=m,
                           fg="white", bg="#1a1a1a", selectcolor="#222",
                           font=("Consolas", 10), command=self.reset_led).pack(anchor="w", padx=20)

        self.breathing_phase = 0
        self.heartbeat_stage = 0

        threading.Thread(target=self.track_input, daemon=True).start()
        self.run_led()

    def reset_led(self):
        self.canvas.itemconfig(self.led_ring, outline="#001122")

    def track_input(self):
        while True:
            pygame.event.pump()
            x = joycon.get_axis(0)
            y = joycon.get_axis(1)

            dx = int(y * SPEED) if abs(y) > DEADZONE else 0
            dy = int(-x * SPEED) if abs(x) > DEADZONE else 0

            if dx or dy:
                pyautogui.moveRel(dx, dy)
                self.root.after(0, lambda: self.update_ui("Moving", dx, dy))
            else:
                self.root.after(0, lambda: self.update_ui("Idle", 0, 0))

            a = joycon.get_button(1)
            b = joycon.get_button(0)
            home = joycon.get_button(3)

            if a:
                pyautogui.click()
                self.root.after(0, lambda: self.status.config(text="Status: Left Click"))

            if b:
                pyautogui.click(button='right')
                self.root.after(0, lambda: self.status.config(text="Status: Right Click"))

            if home:
                pyautogui.hotkey("ctrl", "esc")
                self.root.after(0, lambda: self.status.config(text="Status: Start Menu"))

            time.sleep(REFRESH_DELAY)

    def update_ui(self, text, dx, dy):
        self.status.config(text=f"Status: {text}")
        self.coords.config(text=f"ΔX: {dx} | ΔY: {dy}")

    def run_led(self):
        mode = self.mode.get()

        if mode == "Solid":
            self.canvas.itemconfig(self.led_ring, outline="#3399ff")

        elif mode == "Breathing":
            self.breathing_phase += 0.08
            brightness = int((math.sin(self.breathing_phase) + 1) / 2 * 255)
            color = f"#00{brightness:02x}ff"
            self.canvas.itemconfig(self.led_ring, outline=color)

        elif mode == "Heartbeat":
            if self.heartbeat_stage == 0:
                self.canvas.itemconfig(self.led_ring, outline="#3399ff")
                self.heartbeat_stage = 1
                self.root.after(100, self.run_led)
                return
            else:
                self.canvas.itemconfig(self.led_ring, outline="#001122")
                self.heartbeat_stage = 0
                self.root.after(600, self.run_led)
                return

        elif mode == "Off":
            self.canvas.itemconfig(self.led_ring, outline="#001122")

        self.root.after(30, self.run_led)

# 🚀 Launch
if __name__ == "__main__":
    root = tk.Tk()
    BetterJoy(root)
    root.mainloop()

