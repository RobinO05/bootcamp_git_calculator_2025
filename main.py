def main():
    x = 2.0
    y = 4.0

    print(f"{x} + {y} = {add(x, y)}")


# Operationen:
def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mod(x, y):
    return x%y

def power(x, y):
    if y == 0:
        return 1
    result = x
    for i in range(y):
        result * x
    return result

if __name__ == '__main__':
    main()
