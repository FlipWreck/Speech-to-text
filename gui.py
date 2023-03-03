import time
import tkinter as tk

##here we create a window to keep track of our information gotten from whisper and .wav files

def update_file_contents():
    with open("C:\\Users\\donat\\OneDrive\\Desktop\\copied_over\\information.txt", "r") as file:
        contents = file.read()
    label.config(text=contents)
    window.after(1000, update_file_contents)

window = tk.Tk()
label = tk.Label(window, text="")
label.pack()

update_file_contents()
window.mainloop()
