#!/usr/bin/python3
import json


data = {
    "name" : "zfy",
    "age" : 27
}

jsonstr = json.dumps(data)



print(repr(data))
print(jsonstr)


data2 = json.load(jsonstr)

