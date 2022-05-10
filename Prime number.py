max_value=eval(input("輸入最大值 : "))
print("質數有 : ",end="")
for i in range(2,max_value+1):
    j = i - 1
    while i % j != 0 :
        j = j - 1
    if j == 1:
        print(i,", ",end="")    