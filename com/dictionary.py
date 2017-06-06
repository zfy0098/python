# 字典


dict = {"name" : "zfy" , "age" : 27 }

print("获取字典长度")
print(len(dict))

print(dict["name"])

dict["name"] = "周芳禹"

print(dict["name"])


del dict["age"]

print(dict.keys())
print(dict.values())


print(dict)


print("type(dict) : " , type(dict))


print("name in dict :" , "name" in dict)


print(type("name" in dict))