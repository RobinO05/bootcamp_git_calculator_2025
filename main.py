import time
from unittest import result


def main():
    running = True
    x = 0
    y = 0
    first_operation = True
    while running:
        print("Welcome to your Calculator!")
        print("Main Menu")
        print("Addition - 1")
        print("Subtraktion - 2")
        print("Multiplikation - 3")
        print("Division - 4")
        print("Teilbarkeit - 5")
        print("Potenzen - 6")
        print("Wurzel - 7")
        print("Quit Calculator - 0")
        choosed_option = int(input("Please choose an option: "))

        if not first_operation and choosed_option > 0 and choosed_option <= 7:
            inp1 = str(input("Please enter the first number or press A to take the last result "))
            inp2 = str(input("Please enter the second number or press A to take the last result "))
            if inp1 == "A":
                x = result
            else: 
                x = int(inp1)
            if inp2 == "A":
                y = result
            else:
                y = int(inp2)

        elif choosed_option > 0 and choosed_option <= 7:
            inp1 = str(input("Please enter the first number "))
            inp2 = str(input("Please enter the second number "))
        
            x = int(inp1)
            y = int(inp2)

        if choosed_option == 1:
            result = add(x, y)
        elif choosed_option == 2:
            result = sub(x, y)
        elif choosed_option == 3:
            result = mult(x, y)
        elif choosed_option == 4:
            result = div(x, y)
        elif choosed_option == 5:
            result = mod(x, y)
        elif choosed_option == 6:
            result = power(x, y)
        elif choosed_option == 7:
            result = root(x, y)
        elif choosed_option == 0:
            running = False
        else:
            print("Invalid input")
            continue

        time.sleep(2)
        first_operation = False

# Operationen:
def mult(x, y):
    result = x * y
    print(f"The result is {result}")
    return result

def div(x, y):
    result =  x / y
    print(f"The result is {result}")
    return result

def add(x, y):
    result = x + y
    print(f"The result is {result}")
    return result

def sub(x, y):
    result = x - y
    print(f"The result is {result}")
    return result

def mod(x, y):
    result =  x%y
    print(f"The result is {result}")
    return result

def power(x, y):
    if y == 0:
        return 1
    result = x
    for i in range(y - 1):
        result *= x
    print(f"The result is {result}")
    return result

def root(x,y):
    if y < 2:
        print("Invalid input")
        return
    else:
        result = x**(1/y)
        print(f"The result is {result}")
        return result

if __name__ == '__main__':
    main()
