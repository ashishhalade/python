'''Factorial program'''
NUM = 7
FACTORIAL = 1
if NUM < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif NUM == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, NUM + 1):
        FACTORIAL = FACTORIAL*i
    print("The factorial of", NUM, "is", FACTORIAL)
