def get_valid_num(prompt):
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            print('Invalid input.')
            print()

print('This is a program that multiplies two numbers if their product is less than 1000 or else the two numbers are added')

num1 = get_valid_num('Enter first number: ')
num2 = get_valid_num('Enter second number: ')

product = num1 * num2
sum = num1 + num2

if product <= 1000:
    print(product)
else:
    print(sum)