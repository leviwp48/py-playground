class Calculator:
    def __init__(self):
        self.result = 0
        self.current_text = ""

    def calculate_result(self):
        try:
            self.result = self.evaluate_expression(self.current_text)
            return self.result
        except Exception as e:
            return "Error"

    def clear(self):
        self.current_text = ""

    def add_to_expression(self, value):
        self.current_text += value

    def evaluate_expression(self, expression):
        tokens = self.tokenize(expression)
        postfix = self.infix_to_postfix(tokens)
        result = self.evaluate_postfix(postfix)
        return result

    def tokenize(self, expression):
        operators = set(['+', '-', '*', '/'])
        tokens = []
        num = ""

        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            elif char in operators:
                if num:
                    tokens.append(num)
                    num = ""
                tokens.append(char)

        if num:
            tokens.append(num)

        return tokens

    def infix_to_postfix(self, infix_tokens):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        postfix = []
        stack = []

        for token in infix_tokens:
            if token.isdigit() or ('.' in token):
                postfix.append(token)
            elif token in precedence:
                while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                    postfix.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()

        while stack:
            postfix.append(stack.pop())

        return postfix

    def evaluate_postfix(self, postfix_tokens):
        stack = []

        for token in postfix_tokens:
            if token.isdigit() or ('.' in token):
                stack.append(float(token))
            elif token in {'+', '-', '*', '/'}:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.perform_operation(operand1, operand2, token)
                stack.append(result)

        return stack[0]

    def perform_operation(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ValueError("Division by zero")
            return operand1 / operand2


if __name__ == "__main__":
    calculator = Calculator()

    while True:
        print("\nCurrent expression:", calculator.current_text)
        print("Result:", calculator.calculate_result())
        print("Commands: [0-9], +, -, *, /, C (clear), = (evaluate), Q (quit)")

        user_input = input("Enter command or value: ")

        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'c':
            calculator.clear()
        elif user_input == '=':
            print("Result:", calculator.calculate_result())
            calculator.clear()
        else:
            calculator.add_to_expression(user_input)
