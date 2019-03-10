thisDict = {
    "brand":"ford",
    "Model":"Mustang",
    "year":1964
}
print(thisDict)
print(thisDict["Model"])
x = thisDict.get("brand")
print(x)
thisDict["year"] = 2018
print(thisDict)
for COUNTER in thisDict:
    print(thisDict[COUNTER])
x = input("enter a string:")

if x in thisDict:
    print("yessssssssssss,it is in the dictionary")
else:
    print("noooooo,it is not in the dictionary")
print(len(thisDict))
    