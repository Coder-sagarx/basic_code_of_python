str1=input("enter name 1")
str2=input("enter name 2")
str3=input("enter name 3")

list =[]
list.append(str1)
list.append(str2)
list.append(str3)

print(list)
list.remove("sagar")
list.pop()
print(list)

#check palindrome
pal=["121","121"]
list_copy=pal.copy()
list_copy.reverse()

if(pal==list_copy):
    print("palindrome")
else:
    print("not palindrome") 


