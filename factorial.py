num = int(input("Enter an integer: "))
factorial = 1
if num < 0:
    print("Enter a positive integer")
elif num == 0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
print(f"Hence the factorial of the given number is: {factorial}")