n=int(input("Anna numero "))
p=True
if n <= 1:
    p=False
if n <= 3:
    p=True
if (n % 2 == 0 or n % 3 == 0) and n !=2:
    p=False

i = 5
while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
        p= False
    i += 6
if (p==True):
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")


