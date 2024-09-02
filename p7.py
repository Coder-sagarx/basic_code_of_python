# function 
def sum(a,b):
    return a+b
def mul(c,d):
    return c*d
def dev(a,b):
    return a/b
def sub(a,b):
    return abs(a-b)
def chek(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")    

a=int(input("enter first nu =>"))
b=int(input("enter second nu=>"))
print(sum(a,b))
print(mul(a,b))
print(dev(a,b))
print(sub(a,b))
print(chek(a))
print(chek(b))

arr=[]
for i in range(2,10,2):
    a=input("enter a string =>")
    arr.append(a)
    
print(arr)    




 




