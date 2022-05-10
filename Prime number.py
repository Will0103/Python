max_value=eval(input("輸入最大值 : "))
print("質數有 : ",end="")
for i in range(2,max_value+1):
    for j in range(2,i):
        if i % j == 0:
           break
    else:
        print(i,end=" ")    
        