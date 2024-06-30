num = int(input("Enter an integer: "))
temp = False
if num < 0:
    print("Enter only positive integers")
elif num == 1:
    print(f"{num} is not a prime number")
else:
    for i in range(2,num+1):
        if num%i == 0:
            temp = True
        break
if temp:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")
