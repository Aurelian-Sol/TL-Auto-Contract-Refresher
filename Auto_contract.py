import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import threading
from Random_Green_Contract import run_random_green_contract

running = True

def run_script(output_box):
    global running
    running = True
    threading.Thread(target=run_random_green_contract, args=(output_box,)).start()

def on_exit():
    global running
    running = False
    root.destroy()

root = tk.Tk()
root.title("Throne and Liberty Auto Contract Refresher")
root.protocol("WM_DELETE_WINDOW", on_exit)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

output_box = ScrolledText(frame, wrap=tk.WORD, width=50, height=15)
output_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

run_button = tk.Button(root, text="Run Script", command=lambda: run_script(output_box))
run_button.pack(pady=10)

root.mainloop()
