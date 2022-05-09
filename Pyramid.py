height = eval(input("the height of 金字塔 : "))
for i in range(1,height+1):
    print((height-i)*" ", (2*i-1)*"*")
    