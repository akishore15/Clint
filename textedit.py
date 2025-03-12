import tkinter as tk
from tkinter import filedialog

def savefile():
    fpath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text file", "*.txt")])
    if fpath:
        with open(fpath, "w") as file:
            file.write(text_box.get("1.0", tk.END))

root = tk.Tk()
root.title("Text Editor")

text_box = tk.Text(root)
text_box.pack(fill="both", expand=True)

save_button = tk.Button(root, text="Save", command=savefile)
save_button.pack()

root.mainloop()