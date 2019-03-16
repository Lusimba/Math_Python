blah = [
    6,
    4,
    32,
    48,
    3,
]
y = 0
a = 1
for x in blah:
    y = x + y
print(y)    
for z in blah:
    a = z * a
print(a)    
print(max(blah))
print(min(blah))
blah2 = [
    6,
    4,
    32,
    48,
    3,
    4,
    32,
    48,
]
dup_item = set()
uniq_item = []
for x in blah2:
    uniq_item.append(x)
    dup_item.add(x)
print(dup_item)       
