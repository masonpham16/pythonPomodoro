import tkinter as tk
import time

# Global variables
pomodoro_time = 25 * 60  # 25 minutes
short_break_time = 5 * 60  # 5 minutes
long_break_time = 15 * 60  # 15 minutes
current_time = pomodoro_time
is_running = False
is_pomodoro = True  # True for Pomodoro, False for Break

# Functions
def start_timer():
    global is_running, current_time
    is_running = True
    update_timer()

def pause_timer():
    global is_running
    is_running = False

def reset_timer():
    global current_time, is_pomodoro, is_running
    is_running = False
    if is_pomodoro:
        current_time = pomodoro_time
    else:
        current_time = short_break_time
    update_timer()

def update_timer():
    global current_time, is_running, is_pomodoro
    if is_running:
        if current_time > 0:
            current_time -= 1
            minutes, seconds = divmod(current_time, 60)
            timer_label.config(text=f"{minutes:02}:{seconds:02}")
            root.after(1000, update_timer)
        else:
            if is_pomodoro:
                # Switch to break
                is_pomodoro = False
                current_time = short_break_time
                timer_label.config(text="Break Time!")
                root.after(1000, update_timer)
            else:
                # Switch to pomodoro
                is_pomodoro = True
                current_time = pomodoro_time
                timer_label.config(text="Pomodoro Time!")
                root.after(1000, update_timer)
    else:
        minutes, seconds = divmod(current_time, 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")

# Create the main window
root = tk.Tk()
root.title("MICHELLE'S POMODORO")
root.geometry("480x320")
root.config(bg="limegreen") # set background color to limegreen

# Timer display
timer_label = tk.Label(root, text="25:00", font=("Helvetica", 100), fg="black", bg="limegreen")
timer_label.pack(pady=50)

# Start, Pause, and Reset buttons
start_button = tk.Button(root, text="Start", command=start_timer, font=("Helvetica", 14), bd=0, relief="flat")
start_button.pack(side="left", padx=20)

pause_button = tk.Button(root, text="Pause", command=pause_timer, font=("Helvetica", 14), bd=0, relief="flat")
pause_button.pack(side="left", padx=20)

reset_button = tk.Button(root, text="Reset", command=reset_timer, font=("Helvetica", 14), bd=0, relief="flat")
reset_button.pack(side="left", padx=20)

# Start the Tkinter event loop
root.mainloop()
