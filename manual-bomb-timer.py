import Tkinter as tkr
import keyboard
 
root = None
timer_display = None
 
root = tkr.Tk()
root.geometry("+0+0")
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-alpha", 0.01)
root.resizable(0, 0)
 
timer_display = tkr.Label(root, font=('Trebuchet MS', 30, 'bold'), bg='black')
timer_display.pack()
 
seconds = 45
 
toggle_button = 'num lock'
 
enabled = False
 
print("^|______________________________________________________________^|")
print("^|                                                              ^|")
print("^|      ======== Valorant Bomb Time Indicator ==========        ^|")
print("^|   =====This is not a hack its made for practicing =====      ^|")
print("^|           your skills so you can get better at               ^|")
print("^|            estimating the bomb on/off timings                ^|")
print("^|                                                              ^|")
print("^|      Created by : Gamingforecast.com                         ^|")
print("^|      ___________________________________________________     ^|")
print("^|     This is an AI version it auto detects the bomb plant     ^|")
print("^|                                                              ^|")
print("^|______________________________________________________________^|")
 
 
def countdown(time):
    if time > 0:
        mins, secs = divmod(time, 60)
 
        def color_change(t_time):
            if t_time > 10:
                return 'green'
            elif 8 <= t_time <= 10:
                return 'yellow'
            elif t_time < 8:
                return 'red'
 
        timer_display.config(text="{:02d}:{:02d}".format(mins, secs),
                             fg=color_change(time)), root.after(1000, countdown, time - 1)
    else:
        root.wm_attributes('-alpha', 0.01)
        root.quit()
 
 
def start_countdown():
    root.wm_attributes('-alpha', 0.7)
    countdown(seconds)
 
 
last_state = False
 
while True:
    key_down = keyboard.is_pressed(toggle_button)
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = True
            if enabled:
                start_countdown()
                print("Activated")
            else:
                start_countdown()
            root.mainloop()