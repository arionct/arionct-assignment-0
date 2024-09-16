def add_two_numbers(a, b):
    return a + b

if __name__ == '__main__':
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    print(f'The sum of {a} and {b} is {add_two_numbers(a, b)}')