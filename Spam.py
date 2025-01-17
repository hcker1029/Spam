import tkinter as tk
from tkinter import messagebox

def repeat_sentence():
    sentence = entry_sentence.get()
    try:
        count = int(entry_count.get())
        if not sentence.strip():
            messagebox.showerror("Input Error", "Please enter a valid sentence.")
            return
        if count < 1:
            messagebox.showerror("Input Error", "Repeat count must be at least 1.")
            return
        
        # Enable the text box temporarily to update its content
        output_text.config(state='normal')  
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, (sentence + "\n") * count)  # Add repeated sentence
        output_text.config(state='disabled')  # Make the text box read-only
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for repeat count.")

# Create the main application window
root = tk.Tk()
root.title("Sentence Repeater")

# Input fields and labels
label_sentence = tk.Label(root, text="Enter a sentence:")
label_sentence.pack(pady=5)
entry_sentence = tk.Entry(root, width=40)
entry_sentence.pack(pady=5)

label_count = tk.Label(root, text="How many times to repeat:")
label_count.pack(pady=5)
entry_count = tk.Entry(root, width=10)
entry_count.pack(pady=5)

# Repeat button
btn_repeat = tk.Button(root, text="Repeat", command=repeat_sentence)
btn_repeat.pack(pady=10)

# Output area (read-only)
output_text = tk.Text(root, height=15, width=50, state='disabled')
output_text.pack(pady=10)

# Run the application
root.mainloop()
