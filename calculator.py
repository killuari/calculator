class calculator():
    def calculate(self, eingabe):
        clean_input = eingabe.replace("/",",").replace("*",",").replace("+",",").replace("-",",-")
        numbers = [float(i) for i in clean_input.split(",") if i != ""]
        operators = ["+" if i == "-" else i for i in eingabe if i in "*/+-"]
        print(numbers)
        print(operators)
        


    def operate(self, x, operator, y):
        if operator == "/": return x/y
        elif operator == "*": return x*y
        elif operator == "+": return x+y

c = calculator()
ei = "300*42+52-2*-4+9/85.333-0"
print(ei)
c.calculate(ei)
print(ei)