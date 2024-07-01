num = int(input("Enter an interger: "))
num1 = str(num)
no_of_digits = len(num1)

sum_of_digits = 0
temp_num = num

while temp_num > 0:
    rem = temp_num % 10
    sum_of_digits += rem ** no_of_digits
    temp_num //= 10

if sum_of_digits == num:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")
