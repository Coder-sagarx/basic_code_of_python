#list and set can not be a key  bacause it is mutable 
info = {
    "key":"value",
    "name":["sagar","singh","bisht"],
    "subject":{
        "math":78,
        "phy":89,
        "chem":89
    },
    "learning":"coding",
    ("ok"):"sagar",

}

for val in info["subject"]:
    print(val)

print(info.keys())
print(info.values())
print(len(info))  
print(info.items()) 
info.update({"x":"y"}) 
print(info)


