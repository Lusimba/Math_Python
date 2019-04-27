tup1 = ("blah","ya yeat")
numTup = (1,2,3,4,5,6,7,8,9)
print(numTup[2])
tupp1 = (1,2,3,4)
addingItem = (5,)
finalTup = tupp1 + addingItem
print(finalTup)
str = ','.join(tup1)
print(str)
list1 = ["what ","the ","heck ","are ","you ","doing"]
tupp2 = tuple(list1)
print(tupp2)
len(numTup)
T=('C++', 'Java', 'Python') 
new_tup = T[::-1] 
print(new_tup)
def cm_to_m(cm):
    assert(cm>=0),"what the heck"
    print (cm/100,"in meter")
cm = float(input("enter a number: "))
cm_to_m(cm)
try:
    a = 10/0
    print(a)
except Exception as ex:
    print("that is not possible")


    