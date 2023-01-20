from calculator import  calculator as cal

c = cal()
a = int(input('Enter a: '))
b = int(input('Enter b: '))
op = input('Enter operation type symbol * + / - ')
if op == '+':
    c.add(a, b)
elif op == '*':
    c.multiply(a, b)
elif op == '-':
    c.subtruct(a, b)
elif op == '/':
    c.divide(a, b)
else:
    print('You entered an invalid operation type')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
