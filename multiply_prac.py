from mymodule import get_valid_num as validNumCheck  # type: ignore

print('This is a program that multiplies two numbers if their product is less than 1000 or else the two numbers are added')

num1 = validNumCheck('Enter first number: ')
num2 = validNumCheck('Enter second number: ')

product = num1 * num2
sum = num1 + num2

if product <= 1000:
    print(product)
else:
    print(sum)