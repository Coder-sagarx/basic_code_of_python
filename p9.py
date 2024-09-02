# file system

f=open("log.txt","a")
f.write(input("enetr string =>"))
f.close()

with open("log.txt","r") as f:
    print(f.read())

f.close()

with open("log.txt","r") as f:
    data=f.read()
    if(data.find("name")!=-1):
        print("found")     
    else:
        print("not found")    
f.close()   


