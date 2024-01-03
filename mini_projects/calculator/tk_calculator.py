import tkinter as tk

class Calculator:
    def __init__(self):
        self.result = 0
        self.current_text = ""

    def calculate_result(self):
        try:
            self.result = eval(self.current_text)
            return str(self.result)
        except Exception as e:
            return "Error"

class CalculatorUI:
    def __init__(self, root, calculator):
        self.root = root
        self.root.title("Simple Calculator")
        self.calculator = calculator

        self.create_ui()

    def create_ui(self):
        # Entry widget for displaying the input and result
        self.entry = tk.Entry(self.root, width=16, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Create buttons and add them to the grid
        for (text, row, col) in buttons:
            if text == 'C':
                button = tk.Button(self.root, bg='orange', text=text, padx=20, pady=20, font=('Arial', 16), command=lambda t=text: self.on_button_click(t))
            else:
                button = tk.Button(self.root, bg='orange', text=text, padx=20, pady=20, font=('Arial', 16), command=lambda t=text: self.on_button_click(t))

            button.grid(row=row, column=col)

    def on_button_click(self, value):
        if value == '=':
            self.calculator.current_text = self.entry.get()
            result = self.calculator.calculate_result()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        elif value == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.calculator.current_text += value
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    calculator = Calculator()
    root = tk.Tk()
    app = CalculatorUI(root, calculator)
    root.mainloop()
