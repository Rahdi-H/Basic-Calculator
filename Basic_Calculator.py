def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + '\n')
    
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + '\n')

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + '\n')

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + '\n')

while True:
    print('A: for addition')
    print('S: for subtraction')
    print('M: for multiplication')
    print("D: for division")
    print('E: for exit')

    choice = input('enter what you want to do: ')

    if choice == 'a' or choice == "A":
        f = int(input('Enter first number'))
        s = int(input('Enter second number'))
        add(f, s)
    elif choice == 's' or choice == "s":
        f = int(input('Enter first number'))
        s = int(input('Enter second number'))
        sub(f, s)
    elif choice == 'm' or choice == "M":
        f = int(input('Enter first number'))
        s = int(input('Enter second number'))
        mul(f, s)
    elif choice == 'd' or choice == "D":
        f = int(input('Enter first number'))
        s = int(input('Enter second number'))
        div(f, s)
    elif choice == 'e' or choice == "E":
        print('program exited' + '\n')
        quit()
    else:
        print('enter a valid alphabet' + '\n')