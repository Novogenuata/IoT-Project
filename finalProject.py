import tkinter as tk
import threading
import RPi.GPIO as GPIO
import time
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# GPIO pin configuration
GPIO.setmode(GPIO.BCM)
TRIG_PIN = 6
ECHO_PIN = 19
BUZZER_PIN = 18  
RED_BUTTON_PIN = 20
BLUE_BUTTON_PIN = 16
RED_LED_PIN = 17
BLUE_LED_PIN = 22

# the extra window for the security button thing
class SecurityWindow:
    def __init__(self, master, main_window):
        self.master = master
        self.master.title("Security")
        self.master.geometry("200x150")

        self.main_window = main_window
        self.sequence = [] # init sequence
        self.expected_sequence = ["BLUE", "RED", "BLUE"] # expected sequence

        self.label = tk.Label(self.master, text="Please enter the security combo") # default label
        self.label.pack(pady=5)

        self.status_label = tk.Label(self.master, textvariable=self.main_window.security_status)
        self.status_label.pack(pady=5)

        # Set up button events
        try: # try catch just in case some error happens
            GPIO.add_event_detect(RED_BUTTON_PIN, GPIO.FALLING, callback=self.red_pressed, bouncetime=300)
            GPIO.add_event_detect(BLUE_BUTTON_PIN, GPIO.FALLING, callback=self.blue_pressed, bouncetime=300)
        except Exception as e:
            logging.error("Error setting up GPIO event detection: %s", e)

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.master.after(4000, self.close_window) # after 4 seconds the window will destroy itself

    # functions to detect button presses
    def red_pressed(self, channel):
        if self.main_window.popup_open:
            self.sequence.append("RED") # appends the button color to the sequence list
            self.update_label()

    def blue_pressed(self, channel):
        if self.main_window.popup_open:
            self.sequence.append("BLUE")
            self.update_label()

    def update_label(self):
        self.label.config(text=f"Pressed: {'-'.join(self.sequence)}") # syntax for the sequence

        if len(self.sequence) >= len(self.expected_sequence): # logic for unlocking the system
            if self.sequence == self.expected_sequence:
                self.main_window.security_status.set("Unlocked")
                self.label.config(text="Unlocked", fg="green")
                GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(BLUE_LED_PIN, GPIO.LOW)
                self.main_window.disable_unlock_button() # greys out the unlock button if succesfully unlocked
            else:
                self.main_window.security_status.set("Locked")
                self.label.config(text="Incorrect sequence", fg="red") # displays incorrect sequence, keeps locked, user can try again
                GPIO.output(RED_LED_PIN, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(RED_LED_PIN, GPIO.LOW)
            self.sequence = [] # sequence grabs it

    def on_close(self):
        self.main_window.popup_open = False
        try:
            GPIO.remove_event_detect(RED_BUTTON_PIN) # removes event detection when window is closed
            GPIO.remove_event_detect(BLUE_BUTTON_PIN)
        except Exception as e:
            logging.error("Error removing GPIO event detection: %s", e)
        self.master.destroy()

    def close_window(self):
        self.on_close()

    def reset_status(self):
        self.main_window.security_status.set("Locked")

    def lock_security(self):
        self.main_window.security_status.set("Locked")
        self.on_close()

# main class for the app
class SmartWasteManagementApp:
    def __init__(self, top=None):
        top.geometry("600x450+660+210")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(0, 0)
        top.title("Waste Management")

        #Variables
        self.top = top
        self.security_status = tk.StringVar() # sets the status for the security 
        self.security_status.set("Locked") # default security status is locked
        self.popup_open = False
        self.threshold = tk.StringVar(value="80") # default thresh val
        self.lid_height = tk.StringVar(value="60")  # Set default lid height to 60cm
        self.container_depth = tk.StringVar(value="50")  # Set default container depth to 50cm

        # functional functions
        self.create_widgets()
        self.initialize_gpio()
        self.start_gpio_thread()
        self.update_waste_level()

    def create_widgets(self): # the whole gui
        tk.Label(self.top, text="Enter threshold level:").place(x=20, y=10)
        self.Threshinput = tk.Entry(self.top, textvariable=self.threshold)
        self.Threshinput.place(x=20, y=40, height=22, width=126)

        tk.Label(self.top, text="Enter lid height (cm):").place(x=20, y=70)  # Label for lid height
        self.LidHeightInput = tk.Entry(self.top, textvariable=self.lid_height)  # Entry for lid height
        self.LidHeightInput.place(x=20, y=100, height=22, width=126)  

        tk.Label(self.top, text="Enter container depth (cm):").place(x=20, y=130)  # Label for container depth
        self.ContainerDepthInput = tk.Entry(self.top, textvariable=self.container_depth)  # Entry for container depth
        self.ContainerDepthInput.place(x=20, y=160, height=22, width=126) 

        self.Securitybutton = tk.Button(self.top, text="Unlock", command=self.open_security_window)
        self.Securitybutton.place(x=50, y=230, height=31, width=71)

        tk.Label(self.top, textvariable=self.security_status).place(x=130, y=200)
        tk.Label(self.top, text="Security").place(x=50, y=200)

        
        self.warning_frame = tk.Frame(self.top, relief='groove', borderwidth="2")
        self.warning_frame.place(x=210, y=170, height=85, width=335)
        self.warning_label = tk.Label(self.warning_frame, text="", fg="red")
        self.warning_label.pack(expand=True)

        tk.Label(self.top, text="Waste level:").place(x=260, y=20)
        self.WasteLevelVariable = tk.Label(self.top, text="")
        self.WasteLevelVariable.place(x=360, y=20)
        self.CurrentDistanceLabel = tk.Label(self.top, text="")
        self.CurrentDistanceLabel.place(x=360, y=40)
        tk.Button(self.top, text="Lock System", command=self.lock_system).place(x=50, y=270, height=31, width=100)

    def initialize_gpio(self): # intitialize everything
        GPIO.setup(RED_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BLUE_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(RED_LED_PIN, GPIO.OUT)
        GPIO.setup(BLUE_LED_PIN, GPIO.OUT)
        GPIO.setup(TRIG_PIN, GPIO.OUT)
        GPIO.setup(ECHO_PIN, GPIO.IN)
        GPIO.setup(BUZZER_PIN, GPIO.OUT)  

    def start_gpio_thread(self): # threading with a daemon thread
        self.gpio_thread = threading.Thread(target=self.run_gpio_tasks, daemon=True)
        self.gpio_thread.start()

    def open_security_window(self): # opens the security window
        if self.security_status.get() == "Locked": # if locked
            self.popup_open = True
            security_window = tk.Toplevel(self.top)
            SecurityWindow(security_window, self)

    def lock_system(self): # Button to lock the sys
        self.security_status.set("Locked")
        for widget in self.top.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()
        self.popup_open = False
        self.enable_unlock_button()

    def disable_unlock_button(self):
        self.Securitybutton.config(state=tk.DISABLED) # disables the unlock button

    def enable_unlock_button(self):
        self.Securitybutton.config(state=tk.NORMAL) # enables the unlock buton

    def read_distance(self): # distance stuff
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)
        while GPIO.input(ECHO_PIN) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO_PIN) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        return round(distance, 2)

    def update_waste_level(self):
        try:
            distance = self.read_distance()

            # Read container depth from entry widget
            container_depth = self.container_depth.get()
            try:
                container_depth = float(container_depth)
            except ValueError:
                container_depth = 0

            # Calculate waste level based on container depth
            if container_depth != 0:
                waste_level = round((1 - (distance / container_depth)) * 100, 2)
            else:
                waste_level = 0

            if waste_level < 0:
                self.WasteLevelVariable.config(text="Out of bounds / lid off") # sometimes it goes negative
            else:
                self.WasteLevelVariable.config(text=f"{waste_level}%")

            self.CurrentDistanceLabel.config(text=f"Current Distance: {distance} cm")

            threshold_value = self.threshold.get()
            try:
                threshold_value = float(threshold_value)
            except ValueError:
                threshold_value = 80 
            if waste_level >= threshold_value:
                self.WasteLevelVariable.config(text="Full, please empty container")

            lid_height = self.lid_height.get()
            try:
                lid_height = float(lid_height)
            except ValueError:
                lid_height = 0

            # Check if distance exceeds lid height and system is locked
            if distance > lid_height and self.security_status.get() == "Locked":
                self.warning_label.config(text="Lid is open while system is locked, close lid")
                GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Sound buzzer
                time.sleep(1)
                GPIO.output(BUZZER_PIN, GPIO.LOW)
            else:
                self.warning_label.config(text="")

        except Exception as e:
            logging.error("Error updating waste level: %s", e)

        self.top.after(1000, self.update_waste_level)

    def run_gpio_tasks(self):
        while True:
            time.sleep(0.1)

if __name__ == '__main__':
    try:
        root = tk.Tk()
        app = SmartWasteManagementApp(root)
        root.mainloop()
    except KeyboardInterrupt: # try catch for the mainloop
        GPIO.cleanup()
