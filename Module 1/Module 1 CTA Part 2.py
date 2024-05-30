#Get num1 value from the user
num1 = int(input('Enter the value for num1: '))
print('You entered a value of',num1,'for num1.')
print()

#Get num2 value from the user
num2 = int(input('Enter the value for num2: '))
if num2 == 0:
    print('num2 cannot be 0, the program will exit.')
    print()
    exit()
else:
    print('You entered a value of',num2,'for num2.')
    print()

#Multiple num1 and num2 together and update the user
product = num1 * num2
print('The product of num1 and num2 is',product)
print()

#Divide num1 by num2 and update the user
quotient = num1 / num2
print('The quotient of num1 and num2 is',quotient)
print()