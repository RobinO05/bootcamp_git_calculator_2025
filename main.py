import time


def main():
    running = True
    x = 0
    y = 0
    while running:
        print("Welcome to your Calculator!")
        print("Main Menu")
        print("Addition - 1")
        print("Subtraktion - 2")
        print("Multiplikation - 3")
        print("Division - 4")
        print("Teilbarkeit - 5")
        print("Potenzen - 6")
        print("Quit Calculator - 0")
        choosed_option = int(input("Please choose an option: "))
        if choosed_option == 1:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number"))
            add(x, y)
            time.sleep(2)
        if choosed_option == 2:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number"))
            sub(x, y)
            time.sleep(2)
        if choosed_option == 3:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number"))
            mult(x, y)
            time.sleep(2)
        if choosed_option == 4:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number"))
            div(x, y)
            time.sleep(2)
        if choosed_option == 5:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number"))
            mod(x, y)
            time.sleep(2)
        if choosed_option == 6:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number"))
            power(x, y)
            time.sleep(2)
        if choosed_option == 0:
            running = False




# Operationen:
def mult(x, y):
    result = x * y
    print(result)
    return result

def div(x, y):
    result =  x / y
    print(result)
    return result

def add(x, y):
    result = x + y
    print(result)
    return result

def sub(x, y):
    result = x - y
    print(result)
    return result

def mod(x, y):
    result =  x%y
    print(result)
    return result

def power(x, y):
    if y == 0:
        return 1
    result = x
    for i in range(y):
        result * x
    print(result)
    return result

if __name__ == '__main__':
    main()
