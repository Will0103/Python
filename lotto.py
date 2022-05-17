def choice():
    return random.choice(range(1,50))

import random
A=[]
while len(A) <6 :
    a=choice()
    if a not in A :
        A.append(a)
A.sort()
print(A)