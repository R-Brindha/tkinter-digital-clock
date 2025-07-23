import tkinter as tk
import time

def update_clock():
    now = time.localtime()

    # Update Date
    date_label.config(text=time.strftime("%d     %m     %y", now))

    # Update Time with AM/PM
    time_label.config(text=time.strftime("%I     %M     %S", now))
    am_pm_label.config(text=time.strftime("%p", now))

    # Update Day
    day_label.config(text=time.strftime("%A", now).upper())

    root.after(1000, update_clock)

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="black")
root.geometry("400x300")

#MAIN FRAME 
main_frame = tk.Frame(root, bg="black")
main_frame.pack(expand=True)

# DATE BLOCK 
date_title = tk.Label(main_frame, text="DATE     MONTH     YEAR", font=("Courier", 20),
                      bg="black", fg="red")
date_title.pack()

date_label = tk.Label(main_frame, font=("DS-Digital", 50), bg="black", fg="red")
date_label.pack()

#TIME BLOCK 
time_title = tk.Label(main_frame, text="HOUR     MINUTE    SECOND", font=("Courier", 19),
                      bg="black", fg="red")
time_title.pack()

time_frame = tk.Frame(main_frame, bg="black")
time_frame.pack()

time_label = tk.Label(time_frame, font=("DS-Digital", 50), bg="black", fg="red")
time_label.pack(side="left")

am_pm_label = tk.Label(time_frame, font=("DS-Digital", 18), bg="black", fg="red", padx=10)
am_pm_label.pack(side="left")

#DAY BLOCK
day_label = tk.Label(main_frame, font=("DS-Digital", 36), bg="black", fg="red")
day_label.pack(pady=20)

update_clock()
root.mainloop()
