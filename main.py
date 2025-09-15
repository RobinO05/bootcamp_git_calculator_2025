running = True
def main():
    x = 0
    y = 0
    while running:
        print("Welcome to your Calculator!")
        print("Main Menu"
              "Addition - 1"
              "Subtraktion - 2"
              "Multiplikation - 3"
              "Division - 4"
              "Quit Calculator - 0")
        choosed_option = int(input("Please choose an option: "))
        if choosed_option == 1:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number"))
            add(x, y)
        if choosed_option == 2:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number"))
            sub(x, y)
        if choosed_option == 3:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number"))
            mult(x, y)
        if choosed_option == 4:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number"))
            div(x, y)
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
