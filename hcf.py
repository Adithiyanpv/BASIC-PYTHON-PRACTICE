num1 = int(input("Enter an integer: "))
num2 = int(input("Enter the another integer: "))

if num1 > num2:
    smaller = num2
else:
    smaller = num1

for i in range(1,smaller+1):
    if num1%i == 0 and num2%i == 0:
        hcf = i
print(f"{hcf} is the HCF of the given two numbers")