import time
import tkinter as tk
from tkinter import ttk

steps = ["Strip started", "Finish strip" ,"Finish rinse 1","Finish degunk", "Finish rinse 2"]
times = []
current_step = 0
current_item = None
strip_times = []
cycle_count = 0
def record_time():
    global current_step, current_item, cycle_count
    times.append(time.time())
    elapsed_time = times[current_step] - times[current_step-1]
    tree.set(current_item, steps[current_step], elapsed_time)
    if current_step == 1:
        cycle_count += 1
        strip_times.append(elapsed_time)
        print(cycle_count)
        strip_time_label.config(text="Strip time: " + str(sum(strip_times)/cycle_count))
    current_step += 1
    if current_step < len(steps):
        label.config(text=steps[current_step])
    else:
        label.config(text=steps[0])
        current_step = 0
        times.clear()
        current_item = tree.insert('', 'end', values=('', '', '', ''))
root = tk.Tk()
root.title('Step Times')
label = tk.Label(root, text=steps[0])
label.pack()
button = tk.Button(root, text='Enter', command=record_time)
button.pack()
tree = ttk.Treeview(root, columns=("Strip started", "Finish strip" ,"Finish rinse 1","Finish degunk", "Finish rinse 2"), show='headings')
for i, step in enumerate(steps):
    tree.heading(steps[i], text=step)
tree.pack()
strip_time_label = tk.Label(root, text="Strip time: ")
strip_time_label.pack()
current_item = tree.insert('', 'end', values=('', '', '', ''))
root.mainloop()