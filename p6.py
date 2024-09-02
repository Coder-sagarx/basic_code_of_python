arr=[]
i=0
while i<5:
    arr.append(i)
    i+=1

for val in arr:
    print(val)
    
 
i=0
while i<5:
    ch=(input("enter char=>"))
    arr.append(ch)
    i+=1
print(arr)
arr.remove(1)
arr.remove("sagar")
arr.pop()
print(arr)

strr=input("eneter a string =>")
for int in strr:
    print(int)


for i in range(2,4):                     
    pass
    

for i in range(95,105,2):
    if(i==97):
        continue
    print(i)

   