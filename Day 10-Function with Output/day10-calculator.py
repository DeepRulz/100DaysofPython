from day10art import logo


def add(n1, n2): return n1 + n2


def sub(n1, n2): return n1 - n2


def mul(n1, n2): return n1 * n2


def div(n1, n2): return n1 / n2


k = 0


def continue_func(ans):
    global k
    while k == 0:
        z = input("Would you like to continue?")
        if z == 'No':
            print("Thank you for using PyCalculator")
            k = 1
            break
        z = input("Would you like to continue with the previous answer?")
        if z == "Yes":
            opr = input("Pick the operation you want to do: ")
            num3 = float(input("Kindly Enter the Next Number: "))
            function = operations[opr]
            n_result = function(ans, num3)
            print(f"{ans} {opr} {num3} = {n_result}")
            continue_func(n_result)
        if z == "No":
            calculate()


operations = {'+': add, '-': sub, '*': mul, '/': div}


def calculate():
    num1 = float(input("Kindly Enter your First Number: "))
    for i in operations:
        print(i)
    ope = input("Pick the operation you want to do: ")
    num2 = float(input("Kindly Enter your Second Number: "))
    function = operations[ope]
    f_result = function(num1, num2)
    print(f"{num1} {ope} {num2} = {f_result}")
    continue_func(f_result)


print(logo)
calculate()
