
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def Calc():
    first_number = int(input("First Number "))

    while True:
        math_operations = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": divide
        }
        for op in math_operations.keys():
            print(op)

        math_operation = input(f"Choose math operation ")
        second_number = int(input("Second Number "))

        result = math_operations[math_operation](first_number, second_number)

        print(f"Result: {result}")

        continue_with_same_num = input("print yes/y if you want to continue with same number ")

        if continue_with_same_num == "y" or continue_with_same_num == "yes":
            first_number = result
        else:
            Calc()

Calc()
