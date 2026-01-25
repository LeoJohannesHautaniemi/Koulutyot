import random
i=0
d=0
while (i<=1000000):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if (x**2+y**2)<1:
        d=d+1
    i=i+1
print((4*d)/i)