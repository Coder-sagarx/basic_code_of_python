# recursion
def fact(n):
    if(n==1):
        return n
    return n*fact(n-1)

def sum(n):
    if(n==0):
        return n
    return n+sum(n-1)

def pri(n,list):
    if(n==1):
        list.append(n)
        return 
    pri(n-1,list)
    list.append(n)

list=[]
nu=int(input("enter a number =>"))
ans=fact(nu)
ans2=sum(nu)
pri(nu,list)
print(ans)
print(ans2)
print(list)

