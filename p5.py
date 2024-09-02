# set 
set={3,43,3,55,4,2,2,"37828"}
print(set)
print(type(set))
print(len(set))

for val in set:
    print(val)
i=1
while i<=5:
    set.add(int(input("enter nu ->")))
    i=i+1

print(set)   
print(len(set))     

set.remove(55)
print(set)

set.pop()
print(set)

set.clear()
print(set)

set1={37,4,32,54,54,1,1,}
set2={321,4,3,56,5,6,3,1,8}

x=set1.union(set2)
print(x)

y=set1.intersection(set2)
print(y)

