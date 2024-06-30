n_terms = int(input("How many terms to generate: "))
n1,n2 = 0,1
count =  0
if n_terms < 0:
    print("Enter a positive nummber")
elif n_terms == 1:
    print(n1)
else:
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
printf("Hence the generated fibonacci sequence = ,{nterms}")
