import tkinter as tk 
from tkinter import messagebox 
from gtts import gTTS 
from playsound import playsound 
import os 
def play_text(): 
    text = text_entry.get("1.0", tk.END).strip()   
    if text: 
        try: 
            tts = gTTS(text, lang='en')  
 
            tts.save("output.mp3")   
 
            playsound("output.mp3") 
 
            os.remove("output.mp3") 
        except Exception as e: 
            messagebox.showerror("Error", f"An error occurred: {e}") 
    else: 
        messagebox.showwarning("Warning", "Please enter some text to play.") 
 
def clear_text(): 
    text_entry.delete("1.0", tk.END)  
 
def exit_app(): 
    root.destroy()  
 
root = tk.Tk() 
root.title("Text-to-Speech App") 
root.geometry("400x300") 
 
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40) 
text_entry.pack(pady=10) 
 
 
button_frame = tk.Frame(root) 
button_frame.pack(pady=10) 
 
 
play_button = tk.Button(button_frame, text="Play", command=play_text, bg="red", fg="white", width=10, height=2) 
play_button.pack(side=tk.LEFT, padx=10) 
 
set_button = tk.Button(button_frame, text="Clear", command=clear_text, bg="blue", fg="white", width=10, height=2) 
set_button.pack(side=tk.LEFT, padx=10) 
 
exit_button = tk.Button(button_frame, text="Exit", command=exit_app, bg="green", fg="white", width=10, height=2) 
exit_button.pack(side=tk.LEFT, padx=10) 
 
 
root.mainloop()