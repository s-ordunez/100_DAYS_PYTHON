def calculator():
    def add(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2
    def mult(n1, n2):
        return n1 * n2
    def divide(n1, n2):
        return n1 / n2

    operations = {
        "+" : add,
        "-" : subtract,
        "*" : mult,
        "/" : divide,
    }

    calculate = True
    while calculate:
        n1 = int(input("Type in your first number:\n"))
        additional_calculation = True
        while additional_calculation:
            operation = input("Type in a mathematical operator(+,-,*,/):\n")
            n2 = int(input("Type in your second number:\n"))
            total = operations[operation](n1,n2)

            print(f"{n1} {operation} {n2} = {total}")
            more_math = input("Do you want to working with the previous result?:\n")
            if more_math == "yes":
                n1 = total
            else:
                additional_calculation = False