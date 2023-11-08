import tkinter as tk
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.menuBar = tk.Menu(self.root)
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Close", command=self.end_credits)
        self.actionMenu = tk.Menu(self.menuBar, tearoff=0)
        self.actionMenu.add_command(label="Show Message", command=self.show_message)
        self.menuBar.add_cascade(menu=self.fileMenu, label="File")
        self.menuBar.add_cascade(menu=self.actionMenu, label="Action")
        self.root.config(menu=self.menuBar)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="show messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="show message", font=('Arial', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearBtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearBtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.end_credits)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        if event.keysym == "Return" and event.state == 12:
            self.show_message()

    def end_credits(self):
        if messagebox.askyesno(title="Quit?", message="You feel lucky punk??"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)


MyGUI()
