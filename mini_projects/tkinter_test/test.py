import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("500x500")
root.title("BullyWogs")

label = tk.Label(root, text="Yo whats up!", font=('Roboto', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

button1 = tk.Button(buttonFrame, text="one", font=('Arial', 16))
button1.grid(row=0, column=0, sticky=tk.W+tk.E)
button2 = tk.Button(buttonFrame, text="two", font=('Arial', 16))
button2.grid(row=0, column=1, sticky=tk.W+tk.E)
button3 = tk.Button(buttonFrame, text="three", font=('Arial', 16))
button3.grid(row=0, column=2, sticky=tk.W+tk.E)
buttonFrame.pack(fill="x")

# frm = ttk.Frame(root, padding=100)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=10, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
#
root.mainloop()