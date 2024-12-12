import tkinter as tk
import pyttsx3

def PlayButton():
    text = text_entry.get()
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def exitButton():
    root.destroy()

def setButton():
    text_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Text to Speech")
root.geometry("600x400")

label = tk.Label(root, text="Enter the text:")
label.pack(pady=10)

text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

play_button = tk.Button(button_frame, text="Play", width=7, command=PlayButton)
play_button.pack(side=tk.LEFT, padx=10)

set_button = tk.Button(button_frame, text="Set", width=7, command=setButton)
set_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text="Exit", width=7, bg="red", command=exitButton)
exit_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
