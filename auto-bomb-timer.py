import tkinter as tkr

from python_imagesearch.imagesearch import imagesearch

root = tkr.Tk()
root.geometry("+0+0")
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-alpha", 0.01)
root.resizable(0, 0)

timer_display = tkr.Label(root, font=('Trebuchet MS', 30, 'bold'), bg='black')
timer_display.pack()

seconds = 45

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
            elif 7 <= t_time <= 10:
                return 'yellow'
            elif t_time < 7:
                return 'red'

        timer_display.config(text="{:02d}:{:02d}".format(mins, secs),
                             fg=color_change(time)), root.after(1000, countdown, time - 1)
    else:
        root.wm_attributes('-alpha', 0.01)
        search_image()


def start_countdown():
    root.wm_attributes('-alpha', 0.7)
    countdown(seconds)


def search_image():
    pos = imagesearch("./github.png")
    pos1 = imagesearch("./github1.png")
    if pos[0] & pos1[0] != -1:
        start_countdown()
    else:
        root.after(100, search_image)


root.after(100, search_image)
root.mainloop()
